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
                    <b-link href="#foo">
                        {{city.pharmacy_name}}, ул.
                        {{city.street}},
                        {{city.house}}, тел.
                        {{city.phone}}
                    </b-link>
                </div>
                <div class="itemMap">
                    <b-link href="#foo">
                        <custom-icon name="map-pin" class="custom-icon"/>
                        <i> Посмотреть на карте</i>
                    </b-link>
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

    .wrapper {
        text-align: center;
    }

    .city {
        margin: 5px 0;
        border: 1px solid gray;
        text-align: center;

    }

    .itemMap {
        width: 20%;
        padding: 0.5em;
        align-self: center;
        text-align: center;
    }

    .pharmacyContent {
        width: calc(80% - 1em);
        margin-left: 1em;
        display: flex;
        flex-wrap: wrap;
        align-content: center;
    }

    .custom-icon {
        width: 24px;
    }

</style>