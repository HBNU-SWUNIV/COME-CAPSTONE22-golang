const express = require('express');
const router = express.Router();
let pool = require('../config/config');
const { Sales } = require('../models/index.js');

router.get('/data/:id', async (req, res, next)=>{
    await pool.getConnection((err,conn)=>{
        if(err) console.error(err);
        let sql = `select STRAIGHT_JOIN sa.Sales_buyer, sa.Sales_amount, sa.Sales_date, sa.Sales_price, p.Product_name, sa.Sales_id  
        from Sales sa left join product p on sa.Product_id = p.Product_id WHERE p.Coop_id = ${req.params.id}`;
        conn.query(sql,(err,result)=>{
          conn.release();
          if(err){
            console.error(err);
          }
          res.send(result);
        })
      })
})


router.delete('/delete/:id', async (req,res,next)=>{
    if(!req.params.id){
        res.status(500).send('ID is not exist.');
        return ;
    }

    await Sales.destroy(
        {where: {Sales_id: req.params.id}}
    ).catch((err)=>{
        console.log("delete Error: ", err);
    })
    res.send('');
})


router.post('/registration', async (req, res, next)=>{
    await Sales.create({
        Product_id: req.body.product,
        Sales_amount: req.body.amount,
        Sales_price: req.body.price,
        Sales_date: req.body.date,
        Sales_buyer: req.body.buyer,
    }).then(_ => console.log("Data is created!"));
    res.send('');
})


router.get('/shipment/:id',async (req,res,next)=>{
    await pool.getConnection((err,conn)=>{

        let sql2 = `UPDATE product as p, Sales as s SET p.Total_amount = p.Total_amount - s.Sales_amount WHERE s.Sales_id = ${req.params.id} AND p.Product_id = s.Product_id;`
        conn.query(sql2,(err,result)=>{
          if(err){
            console.error(err);
            res.status(500).send('internal Serve Error');
          }
        });

        let sql = `INSERT into Shipment(Shipment_date, Shipment_amount, Shipment_price,Product_id, Shipment_buyer)
        SELECT Sales_date,Sales_amount,Sales_price,Product_id ,Sales_buyer FROM Sales WHERE Sales_id = ${req.params.id}
        `
        conn.query(sql,(err,result)=>{
            conn.release();
            if(err){
                console.error(err);
            }
            res.send('');
        })
    })
})


module.exports = router;