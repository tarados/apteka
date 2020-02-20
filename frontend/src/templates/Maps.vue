<template>
    <div class="App">
        <b-button squared variant="outline-danger">Button</b-button>
    </div>
</template>

<script>
    import MarkerClusterer from '@google/markerclusterer';
    import gmapsInit from '../utils/gmaps.js';
    export default {
        props: {
            locations: {
                type: Array
            }
        },
        data() {
            return {
                count: 0
            }
        },
        methods: {

        },
        async mounted() {
            // eslint-disable-next-line no-console
            console.log(this.locations);
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
                    map.setZoom(15);
                    // map.fitBounds(results[0].geometry.viewport);
                });

                const markerClickHandler = (marker) => {
                    map.setZoom(13);
                    map.setCenter(marker.getPosition());
                };

                const markers = this.locations
                    .map((location) => {
                        const marker = new google.maps.Marker({...location, map});
                        marker.addListener(`click`, () => markerClickHandler(marker));

                        return marker;
                    });

                // eslint-disable-next-line no-new
                new MarkerClusterer(map, markers, {
                    imagePath: `https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m`,
                });
            } catch (error) {
                // eslint-disable-next-line no-console
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
        height: 100vh;
    }
</style>
