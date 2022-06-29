const rpta = document.getElementById('resultado');
const botones = document.querySelectorAll('.botones span');

botones.forEach(e => {
    e.addEventListener('click', (btn)=>{
        const btnValor = btn.target.innerHTML;
        
        if(isNaN(btnValor) === false){
            if(rpta.innerHTML.length < 16){
                rpta.innerHTML += eval(btnValor);
            }

        }else if(btnValor === '='){
            if(rpta.innerHTML !== '' && isNaN(rpta.innerHTML.substr(-1)) === false){
                rpta.innerHTML = eval(rpta.innerHTML);
            }

        }else if(btnValor === 'CE'){
            rpta.innerHTML = rpta.innerHTML.substr(0 ,rpta.innerHTML.length - 1);

        }else if(btnValor === 'C'){
            rpta.innerHTML = '';

        }else{
            if(isNaN(rpta.innerHTML.substr(-1)) === false){
                rpta.innerHTML += btnValor;
            }else{
                rpta.innerHTML = rpta.innerHTML.substr(0, rpta.innerHTML.length -1) + btnValor;
            }
        }    
    });
})


setInterval(() => { //Ejecutar fecha cada segundo
    let fecha = new Date();
    const meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'];
    const dias = ['Domingo','Lunes','Martes','Miércoles','Jueves','Viernes','Sábado'];
    const mes = meses[fecha.getMonth()];
    const dia = dias[fecha.getDay()];
    const diaN = fecha.getDate();
    const horas = (String(fecha.getHours()).length == 2) ? fecha.getHours() : `0${fecha.getHours()}`;
    const minutos = (String(fecha.getMinutes()).length == 2) ? fecha.getMinutes() : `0${fecha.getMinutes()}`;
    const segundos = (String(fecha.getSeconds()).length == 2) ? fecha.getSeconds() : `0${fecha.getSeconds()}`;

    //Mostrando fecha
    document.getElementById('dia').innerHTML = dia;
    document.getElementById('mes').innerHTML = `${diaN} ${mes}`;
    document.querySelector('#hora p:nth-child(1)').innerHTML = horas;
    document.querySelector('#hora p:nth-child(2)').innerHTML = minutos;
    document.querySelector('#hora p:nth-child(3)').innerHTML = segundos;
}, 1000);




language="JavaScript"

var input = document.querySelector("reloj")
function mueveReloj(){
    momentoActual = new Date()
    hora = momentoActual.getHours()
    minuto = momentoActual.getMinutes()
    segundo = momentoActual.getSeconds()

    str_segundo = new String (segundo)
    if (str_segundo.length == 1)
       segundo = "0" + segundo

    str_minuto = new String (minuto)
    if (str_minuto.length == 1)
       minuto = "0" + minuto

    str_hora = new String (hora)
    if (str_hora.length == 1)
       hora = "0" + hora

    horaImprimible = hora + " : " + minuto + " : " + segundo

    reloj.value = horaImprimible

    setTimeout("mueveReloj()",1000)
}





  $(function() 
  {
    $("#mi-formulario").validate({
         rules: {
                email: {
                    required: true,
                    email: true
                },
                password: "required",
                fono: "required",
                fecha: "required",
                password2: {
                    required: true,
                    equalTo: "#password"
                }                       
            }, //rules
        messages: {
            email: {
                required: 'Ingresa tu correo electrónico',
                email: 'Formato de correo no válido'
            },
            password: {
                required: 'Ingresa una contraseña',
                minlength: 'Caracteres insuficientes'
            },
            nombre:{
                required: 'Ingrese su nombre',
                minlength: 'Nombre no valido o muy corto'
            },
            fecha:{
                required: 'Seleccione una fecha válida',
                min: 'Fecha no corresponde'
            },
            password2: {
                required: 'Reingresa la contraseña',
                equalTo: 'Las contraseñas ingresadas no coinciden',
                minlength: 'Caracteres insuficientes'
            }
        }//messages
    }); //$('#mi-formulario').validate
}); //function



function CambiaColor(a)
{
a.style.background = "aqua";
}





function CambiarMayusculas()
    {
        var a = document.getElementById('nom');
        a.value = a.value.toUpperCase();
    }

function Cambiar()
    {
        var a = prompt('Escribe un nuevo titulo: ');
        document.getElementById('titulo').innerHTML = a;
    }

    function mialerta() {  
        alert("¿Esta seguro que sus datos son correctos?");
    } 




    $(function() 
  {
    $("#formulario-contacto").validate({
         rules: {
                email: {
                    required: true,
                    email: true
                },
                telefono: {
                    required: true,
                    telefono: true,
                },

                comuna: {
                    required: true,
                    comuna: true,
                },
                nom:"required,"
                                   
                },
                comentarios:{
                    required:true,
                    comuna: true,
                },//rules
        messages: {
            email: {
                required: 'Ingresa tu correo electrónico',
                email: 'Formato de correo no válido'
            },
            
            nom:{
                required: 'Ingrese su nombre',
                minlength: 'Nombre no valido o muy corto'
            },
            telefono:{
                required: 'Ingrese su telefono',
                minlength: 'Digitos insuficientes'
            },
            comuna: {
                required: 'Seleccione su comuna',
                minlength: 'Seleccione su comuna'
            },
            comentarios:{
                required: 'Ingrese un comentario',
                minlength: 'Ingrese un comentario'
            }
        }//messages
    }); //$('#mi-formulario').validate
}); //function

