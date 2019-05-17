function loadBackground () {
    path = ['cabins', 'castles', 'villas'];
    randomPath = path[Math.floor(Math.random()*path.length)];
    randomImg = Math.floor(Math.random()*4);
    console.log(randomPath);
    console.log(randomImg);
    document.body.style.backgroundImage = "url('../../static/images/"+randomPath+"/0"+randomImg+"_00.jpeg')";
    document.body.style.backgroundSize = 'cover';
}



// $('body').css({'background-image': '../images/'+randomPath+'/0'+randomImg+'_00.jpeg)'});