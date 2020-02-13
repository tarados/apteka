<template>
    <div class="App"></div>
</template>

<script>
    import MarkerClusterer from '@google/markerclusterer';

    import * as axios from "axios";

    import gmapsInit from '../utils/gmaps.js';
    // import * as send from '../send';

    export default {
        data() {
            return {
                payload: [],
                locations: [],
                count: 0,
                url: {
                    index: 'http://127.0.0.1:8000/app/farmacy'
                }
            }
        },
        methods: {
            async getPayload() {
                // const response = await send.get('farmacy');
                const response = await axios.get(this.url.index);
                this.payload = response.data;
                this.payload.pharmacyes.forEach(pharmacy => {
                    const position = {};
                    position['lat'] = pharmacy.latitude;
                    position['lng'] = pharmacy.longitude;
                    const locdata = {position};
                    this.locations.push(locdata);
                });
            }
        },
        async mounted() {
            await this.getPayload();
            try {
                const google = await gmapsInit();
                const geocoder = new google.maps.Geocoder();
                const map = new google.maps.Map(this.$el);


                geocoder.geocode({address: `Donetsk`}, (results, status) => {
                    if (status !== `OK` || !results[0]) {
                        throw new Error(status);
                    }

                    map.setCenter(this.locations[20]);
                    // map.setCenter({ lat: 48.056858, lng: 38.129393});
                    map.setZoom(15);
                    // map.fitBounds(results[0].geometry.viewport);
                });

                const markerClickHandler = (marker) => {
                    map.setZoom(13);
                    map.setCenter(marker.getPosition());
                };

                const location = this.locations[20];
                const marker = new google.maps.Marker({...location, map});
                markerClickHandler(marker);
                // marker.addListener(`click`, () => markerClickHandler(marker));


                // const markers = this.locations
                //     .map((location) => {
                //         const marker = new google.maps.Marker({...location, map});
                //         marker.addListener(`click`, () => markerClickHandler(marker));
                //
                //         return marker;
                //     });

                // eslint-disable-next-line no-new
                new MarkerClusterer(map, marker, {
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
        width: 100vw;
        height: 100vh;
    }
</style>
