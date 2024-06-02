// Function to get color based on count
function getColor(d) {
    return d > 100 ? '#800026' :
           d > 50  ? '#BD0026' :
           d > 20  ? '#E31A1C' :
           d > 10  ? '#FC4E2A' :
           d > 5   ? '#FD8D3C' :
           d > 1   ? '#FEB24C' :
                     '#FFEDA0';
}

// Function to style each feature
function style(feature) {
    return {
        fillColor: getColor(feature.properties.count),
        weight: 2,
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.7
    };
}

// Function to bind popups to features
function onEachFeature(feature, layer) {
    layer.bindPopup('<b>' + feature.properties.name + '</b><br>Count: ' + feature.properties.count);
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight
    });
}

// Highlight feature on hover
function highlightFeature(e) {
    var layer = e.target;
    layer.setStyle({
        weight: 5,
        color: '#666',
        dashArray: '',
        fillOpacity: 0.7
    });

    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    }
}

// Reset highlight
function resetHighlight(e) {
    geojson.resetStyle(e.target);
}

// Create map
var map = L.map('map').setView([20, 0], 2);

// Add OpenStreetMap tiles as the base layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Fetch data from the server and then the GeoJSON for each country
fetch('/data')
    .then(response => response.json())
    .then(data => {
        data.countries.forEach(country => {
            fetch(`/country_geojson/${country}`)
                .then(response => response.json())
                .then(geojsonData => {
                    // Add the GeoJSON layer with style and onEachFeature
                    L.geoJson(geojsonData, {
                        style: style,
                        onEachFeature: onEachFeature
                    }).addTo(map);
                })
                .catch(error => console.error(`Error fetching GeoJSON for ${country}:`, error)); // Log error for specific country
        });
    })
    .catch(error => console.error('Error fetching data:', error)); // Log error for fetching data