import AlgWidgets 2.0

AlgToolButton {
  id: root
  iconName: "substance_save.png"

  function zerofill( number, width ) {
                    var str = "" + number;
                    while ( str.length < width ) {
                        str = "0" + str;
                     }
                    return str;
                }

  onClicked: {
    try{   
        var url = alg.project.url() //get the project location
        var blankProject = url.match(/\.spt$/) //if url ends with .spt then project hasn't been saved
       
        if(blankProject == ".spt"){
            fileDialog.open()//open dialog and save the project
        }else{
            var regexp = /.*.(\d+)\.spp$/ //expression to find the incremented project number ex. _1
            
            //check to see there is an incremeneted number. 
            if (regexp.test(url)) {
                
                var i = 1 + Number(url.match(regexp)[1])//get tje incremented project number
                
                //save the project with the incremented value
                alg.project.save(url.replace(/.(\d+)\.spp$/, "."+zerofill(i, 4)+".spp"))
                
                } else {
                    //project hasn't been incremented yet so add a _1
                    alg.project.save(url.replace(/\.spp$/, ".0001.spp"))
            }
        }
       
        }catch (e){
            alg.log.error(e.message)
        }
  }
}