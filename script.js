var width = 100,
    height = 100;

var raw_data, nested_data, incomeLevel, indicator; //global variable

function formatData() {

    //get the json file
    d3.csv("/data/wb_SE.SCH.LIFE.FE;SE.SCH.LIFE.MA.csv", function (error, csv) {
        if (error) return console.warn(error);
        raw_data = csv;
        nested_data = d3.nest()//http://cs.wellesley.edu/~mashups/pages/am5/d3tutorial2.html
            .key(function (d) {
                return d.country_id;
            })
            .key(function (d) {
                return d.indicator_id;
            })
            .map(raw_data);
    })
}
function visualize(error, countries, data){
    //pass countries with their indicators
    //1. Each country's will be graph in a separate div

    var visualizationWrapper = d3.select("#vis").append("div");

    var svg_country = visualizationWrapper
        .enter()
        .append("svg");

    //You make the svg first by doing select or selectAll,
    // then append a group inside it,
    // because it is easier to do translates on a group
    // (similar to illustrator) and
    // then bind (enter/exit on the svg elements like rect or path)
}

//http://stackoverflow.com/questions/288699/get-the-position-of-a-div-span-tag
/*
 This function will tell you the x,y position of the element
 relative to the page. Basically you have to loop up through
 all the element's parents and add their offsets together.
 */
function getPos(el) {
    // yay readability
    for (var lx=0, ly=0;
         el != null;
         lx += el.offsetLeft, ly += el.offsetTop, el = el.offsetParent);
    return {x: lx,y: ly};
}
formatData();


//
function drawRow(nestedData){

    for(incomeLevel in nestedData) {
        var incomeLevel_data = nestedData[incomeLevel];

        for (indicator in incomeLevel_data) {
            var timeseries = incomeLevel_data[indicator];
            // console.log(timeseries);

            timeseries.forEach(function (d) {
                //       svg.append("svg:path")
                //       .data(d)
                //      .attr("class", "area")
                //      .attr("d", area);
                console.log(d.year);
                console.log(d.value);
            });
        }

    }



}

function drawCol(graphData){


}



