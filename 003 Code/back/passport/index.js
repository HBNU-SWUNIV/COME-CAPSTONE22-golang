const LocalStrategy = require('passport-local').Strategy;
const { coop } = require('../models/index.js');

exports.config = (passport) => {

    passport.serializeUser((user, done) => {
        done(null, user.Coop_login_id);
    });

    passport.deserializeUser(async function(id, done) {
        const result = await coop.findOne({ where: {Coop_login_id: id}});
        done(null, result);
    });

    passport.use(new LocalStrategy({
        usernameField: 'id',
        passwordField: 'password',
        session: true,
        passReqToCallback: false,
    }, async function (id, password, done) {
        try {
            // console.log(id);
            const result = await coop.findOne({
                where: { Coop_login_id: id }
            });
            
            if (password == result.Coop_pw) {
                return done(null, result);
            } else {
                return done(null, false, { message: "Wrong password." });
            }
        } catch (err) {
            return done(null, false, { message: "Wrong id." });
        }
    }));
};