  function checkphone()
{

    var name = document.getElementById("phno").value;
    var param = 'phno='+name;
    var req = new XMLHttpRequest();
    req.onreadystatechange = show;
    req.open("POST","http://127.0.0.1:8000/searcphone/",true);
    req.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    req.send(param);

     function show()
               {
                if(req.readyState == 4)
                       {
                         var v = req.responseText;
                         var json_data = JSON.parse(v);
                          if(json_data.error=='phone no is taken'){
                            document.getElementById('sp_ph').innerText =json_data.error;
                            document.getElementById('b1').disabled=true
                               }

                          else{
                            document.getElementById('sp_ph').innerText = json_data.message;
                            document.getElementById('b1').disabled=false;
                          }
                       }
               }
  }

  function checkemail()
{

    var name = document.getElementById("email").value;
    var param = 'email='+name;
    var req = new XMLHttpRequest();
    req.onreadystatechange = show;
    req.open("POST","http://127.0.0.1:8000/searchemail/",true);
    req.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    req.send(param);

     function show()
               {
                if(req.readyState == 4)
                       {
                         var v = req.responseText;
                         var json_data = JSON.parse(v);
                          if(json_data.error=='this email is taken'){
                            document.getElementById('sp_email').innerText =json_data.error;
                            document.getElementById('b1').disabled=true;
                               }

                          else{
                            document.getElementById('sp_email').innerText = json_data.message;
                            document.getElementById('b1').disabled=false;
                          }
                       }
               }
  }
