const express = require('express');
const { off } = require('../config/config');
const router = express.Router();
let pool = require('../config/config');

router.post('/registration',async (req,res,next)=>{

  await pool.getConnection((err,conn)=>{
      if(err) console.error(err);
      let sql =`INSERT INTO product(Product_name,Product_category,Product_unit,Product_price,Coop_id) 
      VALUES("${req.body.name}","${req.body.category}","${req.body.unit}","${req.body.price}","${req.body.coop}");`; 
      conn.query(sql,(err,result)=>{
        conn.release();
        if(err){
          console.error(err);
        } 
        res.send('INSERT success');
        console.log('1 record inserted');
      });
  });

});

router.get('/data/:id',async (req,res,next)=>{
  await pool.getConnection((err,conn)=>{
    if(err) console.error(err);
    let sql = `SELECT * FROM product WHERE Coop_id = ${req.params.id} ;`;
    conn.query(sql ,(err,result)=>{
      conn.release();
      if(err){ 
        console.error(err);
      }
      res.send(result);
    });
  });
});

router.delete('/delete/:id',async (req,res,next)=>{
  if(!req.params.id){
    res.status(500).send('ID is not exist.');
    return;
  }

  await pool.getConnection((err,conn)=>{
    if(err) console.error(err);
    let sql = `DELETE FROM product WHERE Product_id = ${req.params.id};`;
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

module.exports = router;





  
  // app.get('/api/user/data',(req,res)=>{
  //   db.query('SELECT * FROM coopMember',(err,rows,fields)=>{
  //     console.log(rows);
  //     console.log(fields);
  //   });
  // });