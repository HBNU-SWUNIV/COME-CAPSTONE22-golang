const express = require('express');
const { off } = require('../config/config');
const router = express.Router();
let pool = require('../config/config');
const { coopMember } = require('../models/index');

router.post('/registration',async (req,res,next)=>{

  await pool.getConnection((err,conn)=>{
      if(err) console.error(err);
      let sql =`INSERT INTO coopMember(Member_name,Member_address,Member_pw,Member_phone,Coop_id,Member_area) 
      VALUES("${req.body.name}","${req.body.address}","${req.body.password}","${req.body.phone}","${req.body.coop}","${req.body.area}");`; 
      conn.query(sql,(err,result)=>{
        conn.release();
        if(err){
          console.error(err);
        }
        console.log('1 record inserted');
        res.send('INSERT success');
        

      });
  });

});



router.get('/data/:id',async(req,res,next)=>{


  await pool.getConnection((err,conn)=>{
    if(err) console.error(err);

    let sql = `SELECT * FROM coopMember WHERE Coop_id = "${req.params.id}";`;
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
    let sql = `DELETE FROM coopMember WHERE Member_id = ${req.params.id};`;
    conn.query(sql,(err,result)=>{
      conn.release();
      if(err){  
        console.error(err);
        res.status(500).send('Internal Serve Error');
      }
      res.send({});
    })
  })
})



router.get('/management/:id',async (req,res,next)=>{
  await pool.getConnection((err,conn)=>{
    if(err) console.error(err);
    let sql = `SELECT cm.Member_name, MIN(IFNULL(ws.Shipment_date,"-") ) as shipment_date, MIN(IFNULL(ws.Member_update_date,"-")) as update_date 
    FROM coopMember cm left join warehousing_schedule ws on cm.Member_id = ws.Member_id WHERE cm.Coop_id =${req.params.id}
    GROUP BY cm.Member_id`;
    conn.query(sql,(err,result)=>{
      conn.release();
      if(err){
        console.error(err);
      }
      res.send(result);
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