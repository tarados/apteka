<template>
    <div class="wrapper">
        <div class="choice">
            <div class="choiceChild">
                <b-dropdown
                        split
                        split-variant="outline-info"
                        text="Выберите город"
                        variant="info"
                        class="m-2"
                        :class="{ isActive: !state }"
                >
                    <b-dropdown-item v-for="(city, index) in cities" :key="index" @click="getCity(index)">{{ city }}
                    </b-dropdown-item>
                </b-dropdown>
            </div>
            <div class="choiceChild"
                 v-if="choiceCity"
                 :class="{ isActive: !state }"
            >
                <div v-if="mapClose">
                    <b-button
                            @click="showOnMap()"
                            variant="outline-primary"
                    >
                        <custom-icon name="map-pin" class="custom-icon"/>
                        <i> Посмотреть на карте</i>
                    </b-button>
                </div>
                <div v-else>
                    <b-button
                            @click="showOnMap()"
                            variant="outline-primary"
                    >
                        <custom-icon name="map-pin" class="custom-icon"/>
                        <i>Закрыть карту</i>
                    </b-button>
                </div>
            </div>
        </div>
        <div class="filteredCity"
             v-for="(pharmacy) in pharmaciesFiltered" :key="pharmacy.pharmacyId"
             v-show="state"
             :class="{ isActive: mapVisible }"
        >
            <div class="row city">

                <div
                        class="pharmacyContent"
                        :class="{ mapVisible: !mapVisible }"
                >
                    {{pharmacy}}
<!--                    <div class="content">-->
<!--                        {{city.pharmacy_name}}, ул.-->
<!--                        {{city.street}},-->
<!--                        {{city.house}}, тел.-->
<!--                        {{city.phone}}-->
<!--                    </div>-->
                    <div class="pharmacyChoice">
                        <b-button variant="outlineoutline-primary" @click="choiceFarmacy(pharmacy.pharmacyId)">Выберите аптеку</b-button>
                        <b-button variant="outlineoutline-primary" @click="showOnMap('se')">те аптеку</b-button>
                    </div>
                </div>
            </div>
        </div>
<
        <Map
                v-if="mapVisible"
                :locations="state ? selectedLocationsAll:selectedLocations"
                @clickMarker="clickMarker"
        />
    </div>
</template>


<script>
    import Map from './Maps'
    import customIcon from 'vue-icon/lib/vue-feather.esm'
    import * as send from "../send";
    import groupArray from "group-array";

    export default {
        props: {
            visibleButton: {
                type: Boolean
            },
            visibleAfterOrder: {
                type: Boolean
            }
        },
        components: {
            // eslint-disable-next-line vue/no-unused-components
            customIcon,
            Map
        },
        data() {
            return {
                firstName: '',
                lastName: '',
                phoneOrder: '',
                payloads: [],
                cities: [],
                state: true,
                stateMap: false,
                class: '',
                pharmacyChoice: {},
                pharmacyChoiceAll: [],
                filteredCity: [],
                count: 0,
                mapVisible: false,
                listVisible: false,
                mapClose: true,
                locations: []
            }
        },
        computed: {
            selectedLocations() {
                if (!this.pharmacyChoice.pharmacyId) {
                    return []
                }
                return this.locations.filter(item => item.position.pharmacyId === this.pharmacyChoice.pharmacyId);
            },
            selectedLocationsAll() {
                const locdata = [];
                this.locations.forEach(item => {
                    this.pharmacyChoiceAll.forEach(itemPos => {
                        if (Number(item.position.pharmacyId) === itemPos.pharmacyId) {
                            locdata.push(item);
                        }
                    });
                });
                return locdata;
            },
            // eslint-disable-next-line vue/return-in-computed-property
            choiceCity() {
                if (this.pharmacyChoiceAll.length !== 0) {
                    return true;
                }
            },
            pharmaciesFiltered() {
                if (this.pharmacyChoice.pharmacyId) {
                    return this.pharmacyChoiceAll.filter(item => item.pharmacyId === this.pharmacyChoice.pharmacyId);
                } else {
                    return this.pharmacyChoiceAll;
                }
            }
        },
        methods: {
            async getPayload() {
                const response = await send.get('pharmacy');
                this.payloads = response.pharmacyes;

                this.payloads.forEach(pharmacy => {
                    const position = {};
                    const titleContent = pharmacy.pharmacy_name + " , ул. " + pharmacy.street + ". " + pharmacy.house;
                    position['lat'] = pharmacy.latitude;
                    position['lng'] = pharmacy.longitude;
                    position['pharmacyId'] = pharmacy.pharmacyId;
                    position['title'] = titleContent;
                    const locdata = {position};
                    this.locations.push(locdata);
                });
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
                this.pharmacyChoiceAll = filteredList;
            },
            choiceFarmacy(index) {
                this.state = !this.state;
                this.filteredCity.forEach((item) => {
                    this.pharmacyChoice = item[index];
                });
                this.$emit("choiceFarmacy", this.pharmacyChoice);
            },
            choiceFarmacyBack() {
                this.state = !this.state;
                this.mapClose = !this.mapClose;
                this.$emit("choiceFarmacyBack", false);
            },
            showOnMap(ev) {
                if (ev === 'se') {
                    ev = true;
                } else if (ev == 'cl') {
                    ev = false;
                } else {
                    ev = !this.mapVisible;
                }
                this.mapVisible = !this.mapVisible;
                this.mapClose = !this.mapClose;
                this.$emit("showMap", ev);
            },
            clickMarker(pos) {
                let lat = pos.lat();
                let lng = pos.lng();
                let pharmacyFromMap = {};
                this.payloads.forEach(function (item) {
                    if (item.latitude == lat && item.longitude == lng) {
                        pharmacyFromMap = item;
                    }
                });
                this.pharmacyChoice = pharmacyFromMap;
                this.state = !this.state;
                this.mapVisible = !this.mapVisible;
                this.$emit("choiceFarmacyFromMap", pharmacyFromMap);
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
        justify-content: space-between;
        margin: 0 auto;
    }

    .choiceChild {
        align-self: center;
        font-size: calc(0.65em + 0.3vw);
    }

    .wrapper {
        width: 100%;
        text-align: center;
    }

    .city {
        margin: 5px 0;
        border: 1px solid gray;
        text-align: center;

    }

    .itemMap {
        padding: 0.5em;
        align-self: center;
        text-align: center;
    }

    .pharmacyContent {
        width: 100%;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        align-items: center;
    }

    .buttonGroup {
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

    .isActive {
        display: none;
    }

    .mapVisible {
        width: 100%;
    }

    .btn {
        font-size: calc(0.65em + 0.3vw);
    }

    .content {
        font-size: calc(0.6em + 0.3vw);
    }


    @media (max-width: 544px) {
        .pharmacyContent {
            justify-content: center;
        }
    }



</style>