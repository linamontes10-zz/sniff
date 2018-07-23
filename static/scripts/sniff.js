function myMap() {
  var mapProp= {
      center:new google.maps.LatLng(40.7128,-74.0060),
      zoom:10,
  };
  var map=new google.maps.Map(document.getElementById("googleMap"),mapProp);
  
}
