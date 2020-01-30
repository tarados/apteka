<template>
    <div class="wrapper">
        <div class="choice">
            <b-dropdown
                    split
                    split-variant="outline-info"
                    :text="text"
                    variant="info"
                    class="m-2"
            >
                <b-dropdown-item v-for="(city, index) in cities" :key="index" @click="getCity(index)">{{ city }}
                </b-dropdown-item>
            </b-dropdown>
        </div>
        <div class="filteredCity" v-for="(farmacy, index) in filteredCity" :key="index">
            <div class="row city" v-for="(city, index) in farmacy" :key="index">
                <div class="pharmacyContent">
                    <div class="pharmacy_name">{{city.pharmacy_name}}</div>
                    <div class="street">{{city.street}}</div>
                    <div class="house">{{city.house}}</div>
                    <div class="phone">{{city.phone}}</div>
                </div>

                <div class="itemMap">
                    <custom-icon name="map-pin" class="custom-icon"/>
                    <p>Посмотреть на карте</p>
                </div>
            </div>

        </div>
    </div>
</template>


<script>
    import customIcon from 'vue-icon/lib/vue-feather.esm'
    import * as axios from "axios";
    import groupArray from "group-array";

    export default {
        components: {
            // eslint-disable-next-line vue/no-unused-components
            customIcon
        },
        data() {
            return {
                payloads: [],
                cities: [],
                filteredCity: [],
                text: "Выберите город",
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
                this.payloads = response.data.pharmacyes;
                const groupProductList = groupArray(this.payloads, 'city');
                const keys = [];
                for (const key in groupProductList) {
                    keys.push(key);
                }
                this.cities = this.cities.concat(keys).sort();
            },
            getCity(index) {
                this.filteredCity = [];
                const filter = this.cities[index];
                const filteredList = this.payloads.filter(item => item.city.match(filter));
                this.filteredCity.push(filteredList);
            }
        },
        mounted() {
            this.getPayload();
        }
    }
</script>

<style scoped>
    .choice {
        display: flex;
        justify-content: center;
        margin: 0 auto;
    }

    .filteredCity {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        background-color: #6DDCBD;
    }

    .city {
        width: 100%;
        margin: 5px 0;
        border: 1px solid gray;

    }

    .itemMap {
        width: 20%;
        align-self: center;
    }

    .pharmacyContent {
        width: 80%;
        /*display: flex;*/
        /*flex-wrap: wrap;*/
        /*justify-content: space-between;*/
    }

    .custom-icon {
        width: 24px;
    }

</style>