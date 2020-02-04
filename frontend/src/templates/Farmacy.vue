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
        <div class="filteredCity" v-for="(farmacy, ind) in filteredCity" :key="ind" v-show="state">
            <div class="row city" v-for="(city, index) in farmacy" :key="index">
                <div class="pharmacyContent">
                    <div class="content">
                        {{city.pharmacy_name}}, ул.
                        {{city.street}},
                        {{city.house}}, тел.
                        {{city.phone}}
                    </div>
                    <div class="pharmacyChoice">
                        <b-button variant="outline-primary" @click="choiceFarmacy(index)">Выберите аптеку</b-button>
                    </div>
                </div>
                <div class="itemMap">
                    <b-link href="/basket/checkout/maps">
                        <custom-icon name="map-pin" class="custom-icon"/>
                        <i> Посмотреть на карте</i>
                    </b-link>
                </div>
            </div>
        </div>
        <div class="filteredCity" v-show="!state">
            <div class="row city">
                <div class="pharmacyContent">
                    <div class="content">
                        {{pharmacyChoice.pharmacy_name}}, ул.
                        {{pharmacyChoice.street}},
                        {{pharmacyChoice.house}}, тел.
                        {{pharmacyChoice.phone}}
                    </div>
                    <div class="pharmacyChoice">
                        <b-button variant="outline-primary" @click="choiceFarmacyBack()"><custom-icon name="check" class="custom-icon"/></b-button>
                    </div>
                </div>
                <div class="itemMap">
                    <b-link href="/basket/checkout/maps">
                        <custom-icon name="map-pin" class="custom-icon"/>
                        <i> Посмотреть на карте</i>
                    </b-link>
                </div>
            </div>
            <div>
                <b-card bg-variant="light">
                    <b-form-group
                            label-cols-lg="3"
                            label="Личные данные"
                            label-size="lg"
                            label-class="font-weight-bold pt-0"
                            class="mb-0"
                    >
                        <b-form-group
                                label-cols-sm="3"
                                label="Фамилия:"
                                label-align-sm="right"
                                label-for="nested-street"
                        >
                            <b-form-input id="nested-street"></b-form-input>
                        </b-form-group>

                        <b-form-group
                                label-cols-sm="3"
                                label="Имя:"
                                label-align-sm="right"
                                label-for="nested-city"
                        >
                            <b-form-input id="nested-city"></b-form-input>
                        </b-form-group>

                        <b-form-group
                                label-cols-sm="3"
                                label="Телефон:"
                                label-align-sm="right"
                                label-for="nested-state"
                        >
                            <b-form-input id="nested-state"></b-form-input>
                        </b-form-group>
                    </b-form-group>
                </b-card>
            </div>
            <div class="choice">
                <b-button
                        variant="success"
                        class="m-2"
                >
                    Оформить заказ
                </b-button>
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
                state: true,
                pharmacyChoice: {},
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
            },
            choiceFarmacy(index) {
                this.state = !this.state;
                this.filteredCity.forEach((item) => {
                    this.pharmacyChoice = item[index];
                });
            },
            choiceFarmacyBack() {
                this.state = !this.state;
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
        width: calc(80% - 0.8em);
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        align-items: center;
    }

    .content {
        margin-left: 1em;
    }

    .pharmacyChoice {
        margin-right: 1em;
    }

    .custom-icon {
        width: 24px;
    }

</style>