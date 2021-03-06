<template>
    <div class="wrapper">
        <div class="choice">
            <div class="choiceChild">
                <b-dropdown
                        split
                        split-variant="outline-info"
                        :text="choiceCity ? city: 'Выберите город'"
                        variant="info"
                        class="my"
                        :class="{ isActive: mapVisible }"
                        :disabled="!listVisible"
                >
                    <b-dropdown-item v-for="(city, index) in cities" :key="index" @click="getCity(index)">{{ city }}
                    </b-dropdown-item>
                </b-dropdown>
            </div>
            <div class="choiceChild"
                 v-if="choiceCity"
            >
                <div v-if="!mapVisible">
                    <b-button
                            @click="showOnMap()"
                            variant="outline-primary"
                            title="Посмотреть на карте"
                            :class="{ choicePharmacy: !listVisible}"
                    >
                        <custom-icon name="map-pin" class="custom-icon"/>
                        Выбрать на карте
                    </b-button>
                </div>
                <div v-else>
                    <b-button
                            @click="showOnMapClose()"
                            variant="outline-primary"
                            title="Закрыть карту"
                    >
                        <custom-icon name="map-pin" class="custom-icon"/>
                        Закрыть карту
                    </b-button>
                </div>
            </div>
        </div>
        <div class="filteredCity"
             v-for="pharmacy in filteredPharmacies" :key="pharmacy.pharmacyId"
             :class="{ isActive: mapVisible }"
        >
            <div class="row city">
                <div class="pharmacyContent" :class="{ mapVisible: !mapVisible }">
                    <div class="content">
                        {{pharmacy.pharmacy_name}}, ул.
                        {{pharmacy.street}},
                        {{pharmacy.house}}, тел.
                        {{pharmacy.phone}}
                    </div>
                    <div class="pharmacyChoice">
                        <b-button
                                variant="outline-primary"
                                @click="choiceFarmacy(pharmacy.pharmacyId)"
                                :class="{ choicePharmacy: !listVisible}"
                        >
                            Выберите аптеку
                        </b-button>
                        <b-button
                                variant="outline-primary"
                                @click="choiceFarmacyBack()"
                                :class="{ choicePharmacy: listVisible}"
                        >
                            Выбрaть другую аптеку
                        </b-button>
                        <b-button
                                variant="outline-primary"
                                @click="showOnMapPharmacy(pharmacy.pharmacyId)"
                                title="Показать на карте"
                        >
                            <custom-icon name="map-pin" class="custom-icon"/>
                        </b-button>
                    </div>
                </div>
            </div>
        </div>
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
            customIcon,
            Map
        },
        data() {
            return {
                firstName: '',
                lastName: '',
                phoneOrder: '',
                city: '',
                payloads: [],
                cities: [],
                state: true,
                pharmacyChoice: {},
                pharmacyChoiceAll: [],
                filteredCity: [],
                count: 0,
                mapVisible: false,
                listVisible: true,
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
            choiceCity() {
                if (this.pharmacyChoiceAll.length !== 0) {
                    return true;
                }
            },
            filteredPharmacies() {
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
                const filter = this.cities[index];
                this.pharmacyChoiceAll = this.payloads.filter(item => item.city.match(filter));
                this.city = filter;
                this.listVisible = true;

            },
            choiceFarmacy(index) {
                this.pharmacyChoice = this.pharmacyChoiceAll.filter(item => item.pharmacyId === index)[0];
                this.$emit("choiceFarmacy", this.pharmacyChoice);
                this.listVisible = false;
            },
            choiceFarmacyBack() {
                this.pharmacyChoice = {};
                this.state = !this.state;
                this.listVisible = true;
                this.$emit("choiceFarmacyBack", false);
            },
            showOnMap() {
                this.state = true;
                this.mapVisible = true;
                this.$emit("showMap", true);
            },
            showOnMapClose() {
                this.mapVisible = false;
                this.state = true;
                this.pharmacyChoice = {};
                this.$emit("showMap", false);

            },
            showOnMapPharmacy(pharmacyId) {
                this.pharmacyChoice = this.pharmacyChoiceAll.filter(item => item.pharmacyId === pharmacyId)[0]
                this.state = false;
                this.mapVisible = true;
                if (this.mapVisible) {
                    this.$emit("showMap", true);
                } else {
                    this.$emit("showMap", false);
                }
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
                this.state = false;
                this.mapVisible = false;
                this.listVisible = false;
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
        padding: 5px;
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
        width: 70%;
        text-align: left;
    }

    .pharmacyChoice {
        width: 24%;
        margin-right: 1em;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        align-items: center;
    }

    .custom-icon {
        width: 24px;
    }

    .isActive, .choicePharmacy {
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

    .my {
        margin: 0.5rem 0;
    }


    @media (max-width: 544px) {
        .pharmacyContent {
            justify-content: center;
        }
    }


</style>