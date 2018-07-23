function myMap() {
  var mapProp= {
      center:new google.maps.LatLng(40.74,-74.0060),
      zoom:13,
  };
  var map=new google.maps.Map(document.getElementById("googleMap"),mapProp);

  // setting variables equal to latitude and longitude

  var UnionSquare = new google.maps.LatLng(40.7356, -73.9910);
  var MadisonSquare = new google.maps.LatLng(40.7423, -73.9886);
  var ChelseaWaterside = new google.maps.LatLng(40.7489, -74.00756);
  var LeroyStreet = new google.maps.LatLng(40.7304, -74.0110);
  var WashingtonSquare = new google.maps.LatLng(40.7308, -73.9973);

  // setting variables equal to markers at position identified in variables above

  var UnionDP = new google.maps.Marker({position:UnionSquare});
  var MadisonDP = new google.maps.Marker({position:MadisonSquare});
  var ChelseaDP = new google.maps.Marker({position:ChelseaWaterside});
  var LeroyDP = new google.maps.Marker({position:LeroyStreet});
  var WashingtonDP = new google.maps.Marker({position:WashingtonSquare});

  // creating information for each of the markers

  var infoUnionSquare = new google.maps.InfoWindow({
    content: "Union Square Dog Park"
  });
  var infoMadisonSquare = new google.maps.InfoWindow({
    content: "Madison Square Dog Park"
  });
  var infoChelseaWaterside = new google.maps.InfoWindow({
    content: "Chelsea Waterside Dog Park"
  });
  var infoLeroyStreet = new google.maps.InfoWindow({
    content: "Leroy Street Dog Park"
  });
  var infoWashingtonSquare = new google.maps.InfoWindow({
    content: "Washington Square Dog Park"
  });

  // placing markers on the map

  UnionDP.setMap(map);
  MadisonDP.setMap(map);
  ChelseaDP.setMap(map);
  LeroyDP.setMap(map);
  WashingtonDP.setMap(map);

  // placing information on the map

  infoUnionSquare.open(map,UnionDP);
  infoMadisonSquare.open(map,MadisonDP);
  infoChelseaWaterside.open(map,ChelseaDP);
  infoLeroyStreet.open(map,LeroyDP);
  infoWashingtonSquare.open(map,WashingtonDP);
}
