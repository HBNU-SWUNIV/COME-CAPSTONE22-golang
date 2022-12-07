var express = require('express');
const router = express.Router();
let pool = require('../config/config');


router.post('/month/:id', async (req, res, next) => {

    await pool.getConnection((err, conn) => {
        if (err) console.error(err);

        let sql = `select STRAIGHT_JOIN s.Shipment_buyer, s.Shipment_date,s.Shipment_amount,s.Shipment_price, p.Product_name, s.Shipment_id
        from Shipment s
        left join product p on s.Product_id = p.Product_id 
        WHERE p.Coop_id = ${req.params.id}`;
        conn.query(sql, (err, result) => {
            conn.release();
            if (err) {
                console.error(err)
            }

            var shipment = [];
            var price = [];
            for (var i =0; i < 12; i++){
                shipment[i] = 0;
                price[i] = 0;
            }

            for (item in result){
                var month = result[item].Shipment_date.getMonth();
                var amount = result[item].Shipment_amount;
                var sale = result[item].Shipment_price;
                shipment[month] += amount;
                price[month] += sale;
            }

            var data = null;
            if (req.body.form == 'amount'){
                data = {
                    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
                    datasets: [
                        {
                            label: 'Shipment-amount',
                            backgroundColor: 'red',
                            data: shipment
                        },

                    ]
                }
            } else if (req.body.form == 'price'){
                data = {
                    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
                    datasets: [
                        {
                            label: 'Shipment-sales',
                            backgroundColor: 'blue',
                            data: price
                        }
                    ]
                }
            }
            
            res.send(data);
        })
    })
})


module.exports = router;