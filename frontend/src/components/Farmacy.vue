<template>
    <div class="container-fluid">
        <nav class="navbar fixed-top navbar-expand-lg navbar-dark bg-primary">
            <a class="navbar-brand" href="#">Navbar</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo02"
                    aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
                <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
                    <li class="nav-item">
                        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Link</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link disabled" href="#">Disabled</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link active" href="#">Found: {{ count }}</a>
                    </li>
                </ul>
            </div>
        </nav>
        <div class="row content-box">
            <b-table striped hover :items="payload.pharmacyes"></b-table>
        </div>
    </div>
</template>

<script>
    import * as axios from "axios";

    export default {
        data() {
            return {
                payload: [],
                count: 0,
                url: {
                    index: 'http://127.0.0.1:8000/app/farmacy'
                }
            }
        },
        computed: {},
        methods: {
            async getPayload() {
                const response = await axios.get(this.url.index);
                this.payload = response.data;
            }
        },
        mounted() {
            this.getPayload();
        },
        watch: {}
    }
</script>

<style scoped>
    .content-box {
        margin: 70px 0 5px 0;
    }
</style>