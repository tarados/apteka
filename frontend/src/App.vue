<template>
    <div class="container">

        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
            <a class="navbar-brand" href="#">Navbar</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo02"
                    aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
                <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
                    <li class="nav-item active">
                        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Link</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link disabled" href="#">Disabled</a>
                    </li>
                </ul>
                <form class="form-inline my-2 my-lg-0">
                    <input v-model="query" class="form-control mr-sm-2" type="search" placeholder="Search">
                </form>
            </div>
        </nav>
        <div class="row content-box">
            <div class="col-sm content-filter">
                For filter
            </div>
            <div class="col-sm-10 content-zone">
                Content zone
                <div class="price-content" v-for="product in payload.payload">
                    <div class="product-name">
                        {{ product["product"] }}
                    </div>
                    <div class="product-manufacturer">
                        {{ product["manufacturer"] }}
                    </div>
                    <div class="product-price">
                        {{ product["price"] }} руб.
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import * as axios from "axios";

    export default {
        data() {
            return {
                query: "",
                payload: [],
                url: {
                    index: 'http://127.0.0.1:8000'
                }
            }
        },
        methods: {
            async getPayload() {
                const response = await axios.get(this.url.index);
                this.payload = response.data;
            },
            async getPayloadParam(query) {
                const response = await axios.get(this.url.index, {
                    params: {
                        query: query
                    }
                });
                this.payload = response.data;
            }
        },
        mounted() {
            // this.getPayload();
        },
        watch: {
            query: function (seach) {
                console.log(seach);
                if (this.timerId) {
                    console.log("timer", this.timerId);
                    clearTimeout(this.timerId);
                }
                if (seach.length > 3) {
                    this.timerId = setTimeout( () => {
                        this.getPayloadParam(seach);
                        this.timerId = 0;
                    }, 5000);
                }
            }
        }
    }
</script>

<style scoped>
    .content-box {
        margin: 20px 0 5px 0;
        border: 1px solid;
    }

    .content-filter {
        border-right: 1px solid;
    }

    .price-content {
        height: 90px;
        margin-bottom: 10px;
        border: 1px solid;
        border-radius: 5px;
        padding-top: 7px;
        padding-bottom: 7px;
        text-align: center;
    }


</style>
