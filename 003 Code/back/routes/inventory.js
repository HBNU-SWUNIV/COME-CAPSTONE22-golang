const express = require('express');
const router = express.Router();
let pool = require('../config/config');
const { inventory } = require('../models/index.js');
const { route } = require('./warehousing');



router.get('/received/:id',async (req,res,next)=>{
    await pool.getConnection((err,conn)=>{
        if(err) console.error(err);

        let sql = `select STRAIGHT_JOIN iv.Warehousing_id, iv.Warehousing_date, iv.Warehousing_amount, iv.Product_quailty,iv.Price,p.Product_name,cm.Member_name  
        from inventory iv 
        left join product p on iv.Product_id = p.Product_id 
        left join coopMember cm ON iv.Member_id = cm.Member_id 
        WHERE iv.Coop_id = ${req.params.id}`;
        conn.query(sql,(err,result)=>{
            conn.release(); 
            if(err){
                console.error(err)
            }
            res.send(result);
            
        })        
    })
})

router.post('/registration/:id',async (req,res,next)=>{

    await inventory.create({
        Member_id : req.body.member,
        Product_id : req.body.product,
        Warehousing_amount : req.body.amount,
        Warehousing_date : req.body.date,
        Price : req.body.price,
        Product_quailty : req.body.quality,
        Coop_id:req.params.id,
      }).then(_=>console.log('data is created'))

    await pool.getConnection((err,conn)=>{
      let sql = `UPDATE product SET Total_amount = Total_amount + ${req.body.amount} WHERE Product_id = ${req.body.product}`
      conn.query(sql,(err,result)=>{
          conn.release();
          if(err){
              console.error(err);
          }
      })
    })
    res.send('success');
});


router.delete('/delete/:id',async (req,res,next)=>{
    await pool.getConnection((err,conn)=>{

        let sql2 = `UPDATE product as p , inventory as i SET p.Total_amount = p.Total_amount - i.Warehousing_amount WHERE i.Warehousing_id = ${req.params.id} AND p.Product_id = i.Product_id `
        conn.query(sql2,(err,result)=>{
            if(err){
                console.error(err);
            }
        })

        let sql = `DELETE FROM inventory WHERE Warehousing_id = ${req.params.id}`;
        conn.query(sql,(err,result)=>{
            conn.release();
            if(err){
                console.error(err);
            }
            res.send('success');
            
        })
    })
})

router.get('/quantity/:id',async (req,res,next)=>{
    await pool.getConnection((err,conn)=>{
        let sql=`SELECT STRAIGHT_JOIN p.Product_name,IFNULL(sum(ws.Shipment_amount),0) as Shipment_amount,p.Total_amount as Warehousing_amount, p.Product_unit as Unit
        FROM product p 
        left join warehousing_schedule ws on p.Product_id = ws.Product_id  
        WHERE p.Coop_id =${req.params.id}
        GROUP BY p.Product_id `
        conn.query(sql,(err,result)=>{
            conn.release();
            if(err){
                console.error(err);

            }
            res.send(result)
        })
    })
})

module.exports = router;