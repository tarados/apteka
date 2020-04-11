<template>
    <div class="App">
        <b-button squared variant="outline-danger">Button</b-button>
    </div>
</template>

<script>
    import MarkerClusterer from '@google/markerclusterer';
    import gmapsInit from '../utils/gmaps.js';
    import gmaps from "../utils/gmaps";

    export default {
        props: {
            locations: {
                type: Array
            }
        },
        data() {
            return {
                count: 0,
            }
        },
        methods: {},
        async mounted() {
            try {
                const google = await gmapsInit();
                const geocoder = new google.maps.Geocoder();
                const map = new google.maps.Map(this.$el);

                this.locations.forEach(function (item) {
                    delete item.pharmacyId;
                });


                geocoder.geocode({address: `Donetsk`}, (results, status) => {
                    if (status !== `OK` || !results[0]) {
                        throw new Error(status);
                    }

                    map.setCenter(this.locations[0].position);
                    this.locations.length < 2 ? map.setZoom(15) : map.setZoom(12);
                });


                const markerClickHandler = (marker) => {
                    let p = marker.getPosition();
                    this.$emit("clickMarker", p);
                    // map.setZoom(13);
                    map.setCenter(marker.getPosition());
                };

                const markers = this.locations
                    .map((location) => {
                        const pharmacyId = location.position.pharmacyId;
                        const marker = new google.maps.Marker({
                            ...location,
                            map,
                            title: location.position.title
                        });
                        marker.addListener(`click`, () => markerClickHandler(marker));
                        return marker;
                    });



                new MarkerClusterer(map, markers, {
                    imagePath: `https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m`,
                });

            } catch (error) {
                console.error(error);
            }
        },
    };
</script>

<style scoped>
    html,
    body {
        margin: 0;
        padding: 0;
    }

    .App {
        width: 100%;
        height: 80vh;
    }
</style>
