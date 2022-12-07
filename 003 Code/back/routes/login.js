const express = require('express');
const passport = require('passport');
const router = express.Router();
const { coop } = require('../models/index.js');


router.get('/signIn', function(req, res, next) {
    if (req.isAuthenticated() && req.user) {
        return res.json({ user: req.user });
    }
    
    return res.json({ user: null });
});

router.post('/signIn', function(req, res, next) {
    if (req.isAuthenticated()) {
        return res.redirect('/');
    }
    passport.authenticate('local', (authError, user, info) => {
        if (authError) {
            console.error(authError);
            return next(authError);
        }
        if (!user) {
            return res.json(info);
        }
        return req.login(user, (loginError) => {
            if (loginError) {
                console.error(loginError);
                return next(loginError);
            }
            return res.json({ user });
        });
    })(req, res, next);     // 미들웨어 호출
});

router.post('/signUp', async (req, res, next) => {
    await coop.create({
        Coop_name: req.body.coop,
        Coop_address: req.body.address,
        Coop_pw: req.body.password,
        Coop_login_id: req.body.id
    }).then(_ => console.log("Data is created!"));
    res.send('success');
});

module.exports = router;