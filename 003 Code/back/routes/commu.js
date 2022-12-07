const express = require('express');
const router = express.Router();
let pool = require('../config/config');
const { Commu,Comment } = require('../models/index.js');

router.get('/post/:id', async (req, res, next)=>{
    await pool.getConnection((err,conn)=>{
        if(err) console.error(err);
        let sql = `select c.post_id,c.post_category ,c.\`text\`, DATE_FORMAT(c.post_date,'%Y-%m-%d')as post_date,c.author from Commu as c WHERE c.Coop_id = ${req.params.id} `;
        conn.query(sql,(err,result)=>{
          conn.release();
          if(err){
            console.error(err);
          }
          res.send(result);
        })
      })
})



router.post('/registration/:id', async (req, res, next)=>{
  console.log(req.body.updateDate)
    await Commu.create({
        post_category:req.body.category,
        author:req.body.author,   
        text:req.body.text,
        post_date: req.body.updateDate,
        Coop_id:req.params.id,

    }).then(_ => console.log("Data is created!"));
    res.send('');
})



router.get('/comment/:id',async(req,res,next)=>{
  await pool.getConnection((err,conn)=>{
    let sql = `SELECT author, post_id ,comment_id,author,comment, DATE_FORMAT(post_date,'%Y-%m-%d') as post_date FROM Comment WHERE post_id = ${req.params.id}`
    conn.query(sql,(err,result)=>{
      conn.release();
      if(err){
        console.error(err);
      }
      res.send(result)
    })
  })

})

router.post('/comment/:id',async(req,res,next)=>{
  console.log(req.body.postDate)
  await Comment.create({
    post_id:req.params.id,
    author:'admin',
    comment:req.body.text,
    post_date:req.body.postDate,
  }).then(_ => console.log("Data is created!"));
  res.send('');

})
module.exports = router;