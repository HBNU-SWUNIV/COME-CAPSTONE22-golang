var express = require('express');
const router = express.Router();
const { Shipment } = require('../models/index.js');
let pool = require('../config/config');

router.get('/data/:id',async(req, res, next)=>{

  await pool.getConnection((err,conn)=>{
    if(err) console.error(err);

    let sql = `select STRAIGHT_JOIN s.Shipment_buyer, s.Shipment_date,s.Shipment_amount,s.Shipment_price, p.Product_name, s.Shipment_id
    from Shipment s
    left join product p on s.Product_id = p.Product_id 
    WHERE p.Coop_id = ${req.params.id}`;
    conn.query(sql,(err,result)=>{
        conn.release(); 
        if(err){
            console.error(err)
        }
        res.send(result);
        
    })        
})

})

router.delete('/delete/:id',async(req,res,next)=>{

  await pool.getConnection((err,conn)=>{
    if (err) console.error(err);

    let sql1 = `UPDATE product as p , Shipment as s SET p.Total_amount = p.Total_amount + s.Shipment_amount WHERE s.Shipment_id = ${req.params.id} AND p.Product_id = s.Product_id ;`
    conn.query(sql1,(err,result)=>{
      if(err){
        console.error(err);
      }
      
    })

    let sql2 = `DELETE FROM Shipment WHERE Shipment_id = ${req.params.id};`;
    conn.query(sql2,(err,result)=>{
      conn.release();
      if(err) console.error(err);

      res.send('');
    })
  })
})


router.post('/registration', async (req, res, next)=>{
  await Shipment.create({
      Product_id: req.body.product,
      Shipment_amount: req.body.amount,
      Shipment_price: req.body.price,
      Shipment_date: req.body.date,
      Shipment_buyer: req.body.buyer,
  }).then(_ => console.log("Data is created!"));

  await pool.getConnection((err,conn)=>{
    let sql = `UPDATE product SET Total_amount = Total_amount - ${req.body.amount} WHERE Product_id = ${req.body.product}`
    conn.query(sql,(err,result)=>{
        conn.release();
        if(err){
            console.error(err);
        }
    })
  })


  res.send('');
})





module.exports = router;