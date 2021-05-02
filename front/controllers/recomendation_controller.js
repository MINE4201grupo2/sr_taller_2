
 
module.exports.listRecomendations=function(req,res){
    if(req.session.loggedin){
        const connection = require('../db');
 
        var data = req.body;
        //console.log(data)
        // Query song name an popular songs
        connection.query('SELECT user_id FROM users WHERE email = ?',[req.session.email], function (error, results, fields) {
            if(error) throw error
            var userId = results[0].user_id;
            console.log(userId);
            var limit = null;
            if(!data.categoria== 'ALL'){
                limit= 20
            }
            var sql = `CALL getRecomendation (?,?,?)`
            //console.log(inserts)
            connection.query(sql,[userId,data.categoria, limit], function (error, results, fields) {
                if (error) throw error
                //console.log(results[0])

                
                docs=[]
                res.render('pages/recomendations/recomendations',{title: 'getArtists',
                                                                userProfile: { email: req.session.email },
                                                                business: results[0],
                                                                    "jmap" : docs,
                                                                    lat : 40.78854,
                                                                    lng : -73.96374
                                                                })

            });
        });
    }else{res.redirect('/iniciar-sesion');}

}