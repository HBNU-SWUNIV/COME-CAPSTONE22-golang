var express = require('express');
const router = express.Router();
let pool = require('../config/config');
const zmq = require("zeromq")


router.post('/simulate', async (req, res, next) => {

  async function runClient() {
    console.log('Connecting to hello world server…');

    //  Socket to talk to server
    const sock = new zmq.Request();
    sock.connect('tcp://172.17.22.59:5000');


    let s = [req.body.period, req.body.demand, req.body.supply, 'start']
    await sock.send(s);

    const [result] = await sock.receive();
    if(result.toString() == 'end'){
      res.send('end');
    }
  }

  runClient();


})


router.get('/simulate', async (req, res, next) => {

  await pool.getConnection((err, conn) => {
    if (err) console.error(err);

    let sql = `select Sales_amount, Warehousing_amount, Trash_amount, Oversell_request, Inventory FROM Simulate_Sales `;
    conn.query(sql, (err, result) => {
      conn.release();
      if (err) {
        console.error(err)
      }

      var sales = [];
      var ware = [];
      var trash = [];
      var over = [];
      var inventory = [];
      for (item in result) {
        sales[item] = result[item].Sales_amount;
        ware[item] = result[item].Warehousing_amount;
        trash[item] = result[item].Trash_amount;
        over[item] = result[item].Oversell_request;
        inventory[item] = result[item].Inventory;
      }


      // send data
      var data = null;
      data = {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        datasets: [
          {
            label: 'Shipment-quantity',
            backgroundColor: 'red',
            borderWidth: 2,
            borderColor: 'red',
            pointBorderColor: 'red',
            data: sales
          },
          {
            label: 'Warehousing-quantity',
            backgroundColor: 'blue',
            borderWidth: 2,
            borderColor: 'blue',
            pointBorderColor: 'blue',
            data: ware
          },
          {
            label: 'Disuse-quantity',
            backgroundColor: 'green',
            borderWidth: 2,
            borderColor: 'green',
            pointBorderColor: 'green',
            data: trash
          },
          {
            label: 'Oversell-request',
            borderWidth: 2,
            borderColor: 'orange',
            pointBorderColor: 'orange',
            backgroundColor: 'orange',
            data: over
          },
          {
            label: 'Inventory',
            backgroundColor: 'black',
            borderWidth: 2,
            borderColor: 'black',
            pointBorderColor: 'black',
            data: inventory
          },
        ]
      }

      res.send(data);
    })
  })
})


module.exports = router;