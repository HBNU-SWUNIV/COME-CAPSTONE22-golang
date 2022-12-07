const express = require('express');
const { off } = require('../config/config');
const router = express.Router();
let pool = require('../config/config');
const { warehousing_schedule } = require('../models/index.js')


router.get('/stock/:id',(req,res,next)=>{
  pool.getConnection((err,conn)=>{

    if(err) console.error(err); 
    let sql = `select STRAIGHT_JOIN ws.Schedule_id, ws.Shipment_amount, ws.Shipment_date, ws.Req_price, ws.Product_quailty ,p.Product_name,cm.Member_name  
    from warehousing_schedule ws left join product p on ws.Product_id = p.Product_id left join coopMember cm ON ws.Member_id = cm.Member_id 
    WHERE ws.Coop_id = ${req.params.id}` ;
    conn.query(sql,(err,result)=>{
      conn.release();
      if(err){
        console.error(err);
      }
      res.send(result);
    })
  })
})

router.post('/registration/:id',async (req,res,next)=>{
  console.log(req.params.id);
  await warehousing_schedule.create({ 



    Member_id : req.body.member,
    Product_id : req.body.product,
    Shipment_amount : req.body.amount,
    Shipment_date : req.body.date,
    Req_price : req.body.price,
    Product_quailty : req.body.quality,
    Coop_id:req.params.id,

    Member_update_date:req.body.updateDate,

  }).then(_=>console.log('data is created'))
  res.send('');

})

router.delete('/delete/:id',(req,res,next)=>{
  if(!req.params.id){
    res.status(500).send('id is not exist.');
    return ;
  }

  pool.getConnection((err,conn)=>{
    let sql = `DELETE FROM warehousing_schedule WHERE Schedule_id = ${req.params.id}`;
    conn.query(sql,(err,result)=>{
  
      conn.release();
      if(err){
        console.error(err);
        res.status(500).send('Internal Serve Error');
      }
      res.send('success');
    })
    
  })

})

router.get('/received/:id',(req,res,next)=>{
  if(!req.params.id){
    res.status(500).send('id is not exist.');
    return;
  }
  pool.getConnection((err,conn)=>{

    let sql2 = `UPDATE product as p, warehousing_schedule as ws SET p.Total_amount = p.Total_amount + ws.Shipment_amount WHERE ws.Schedule_id = ${req.params.id} AND p.Product_id = ws.Product_id;`
    conn.query(sql2,(err,result)=>{
      if(err){
        console.error(err);
        res.status(500).send('internal Serve Error');
      }
    });

    let sql = `INSERT into inventory(Member_id,Warehousing_amount,Warehousing_date,Coop_id,Product_id,Product_quailty,Price) 
    SELECT Member_id,Shipment_amount, Shipment_date,Coop_id,Product_id,Product_quailty,Req_price FROM warehousing_schedule where Schedule_id = ${req.params.id};`
    conn.query(sql,(err,result)=>{
      conn.release()
      if(err){
        console.error(err);
        res.status(500).send('internal Serve Error');
      }
      res.send('')
    });



  })
})


module.exports = router;





  
  // app.get('/api/user/data',(req,res)=>{
  //   db.query('SELECT * FROM coopMember',(err,rows,fields)=>{
  //     console.log(rows);
  //     console.log(fields);
  //   });
  // });