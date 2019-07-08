<template>
    <div class="hello">
        <h1>{{ msg }}</h1>

        <div id="myMap"></div>
    </div>
</template>

<script>
    import GoogleMapsLoader from 'google-maps'

    export default {
        name: 'hello',
        data() {
            return {
                msg: 'Welcome to Your Vue.js App'
            }
        },
        mounted: function () {
            GoogleMapsLoader.onLoad(function(google) {
                console.log('I just loaded google maps api');
            });
        }

    }
</script>

<style scoped>
    #myMap {
        height: 300px;
        width: 100%;
    }
</style>