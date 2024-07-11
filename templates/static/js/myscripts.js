var map = L.map('map').setView([42.35420, -71.05817], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);


const setRC1WheelState = async (isRC1on) => {
    const fetchResponse = await fetch("/rcwheel1/"+(isRC1on?1:0), {method: 'POST'});
    if (!fetchResponse.ok){
        alert("command not executed by rasp pi....");
    }
}

const setRC2WheelState = async (isRC2on) => {
    const fetchResponse = await fetch("/rcwheel2/"+(isRC2on?1:0), {method: 'POST'});
    if (!fetchResponse.ok){
        alert("command not executed by rasp pi....");
    }
}

function rcwheelOn1(){
    setRC1WheelState(true);
}

function rcwheelOff1(){
    setRC1WheelState(false);
}

function rcwheelOn2(){
    setRC2WheelState(true);
}

function rcwheelOff2(){
    setRC2WheelState(false);
}


function liveUpdateData (){
    const ch1Pts = document.getElementById("ch1");
    const ch2Pts = document.getElementById("ch2");
    const ch3Pts = document.getElementById("ch3");
    const ch4Pts = document.getElementById("ch4");
    const roll = document.getElementById("roll");
    const pitch = document.getElementById("pitch");
    const yaw = document.getElementById("yaw");
    const dataPressure = document.getElementById("pressure");
    const dataTurbidity = document.getElementById("turbidity");

    setInterval(function() {
        fetch("/update_data").then(function(response){
            return response.json();
        }).then(function (data){
            ch1Pts.textContent = data.voltages[0];
            ch2Pts.textContent = data.voltages[1];
            ch3Pts.textContent = data.voltages[2];
            ch4Pts.textContent = data.voltages[3];
            if (data.orientation[0]!=-1){
                roll.textContent = data.orientation[0];
                pitch.textContent= data.orientation[1];
                yaw.textContent  = data.orientation[2];   
            }
            dataPressure.textContent = data.pressure;
            dataTurbidity.textContent = data.turbidity;
        }).catch(function (error){
            console.log(error);
        });
    }, 2000);
}  


document.addEventListener('DOMContentLoaded', function (){
    liveUpdateData();
});