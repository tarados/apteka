<template>
    <div class="container">
        <div v-if="!showMapVisible">
            <div class="header">
                <b-button
                        id="backToBasket"
                        class="checkout"
                        variant="outline-primary"
                        @click="toBasket"
                        :disabled="!visibleButton"
                >
                    <custom-icon name="chevron-left" class="custom-icon"/>
                    Вернуться в корзину
                </b-button>
                <div class="title checkout"> Оформление заказа</div>
            </div>
            <div>
                <b-table striped hover :items="allProducts" :fields="fields"></b-table>
            </div>
            <hr>
            <div class="totalPrice">
                <div>
                    <i>Всего к оплате:</i>
                </div>
                <div class="price" v-text="getTotalPrice + ' руб.'"></div>
            </div>
            <hr>
        </div>

        <Farmacy
                @choiceFarmacy="choiceFarmacy"
                @choiceFarmacyFromMap="choiceFarmacyFromMap"
                @showMap="showMap"
                @choiceFarmacyBack="choiceFarmacyBack"
                :visibleButton="!visibleButton"
                :visibleAfterOrder="visibleButton"
        />
        <Login
                v-if="stateChoice"
                :pharmacyForOrder="pharmacyForOrder"
                @visibleAfterOrder="visibleAfterOrder"
        />
    </div>
</template>

<script>
    import customIcon from 'vue-icon/lib/vue-feather.esm'
    import Farmacy from "./Farmacy";
    import Login from "./Login";
    import {mapGetters} from 'vuex'

    export default {
        name: "Checkout",
        components: {
            customIcon,
            Farmacy,
            Login
        },
        data() {
            return {
                fields: {
                    title: "Наименование",
                    manufacturer: 'Производитель',
                    price: 'Цена',
                    quantity: 'Количество',
                    valueProduct: 'Сумма'
                },
                pharmacyForOrder: Object,
                stateChoice: false,
                showMapVisible: false,
                visibleButton: true
            }
        },
        computed: {
            ...mapGetters(["allProducts"]),
            ...mapGetters(["getTotalPrice"]),
        },
        methods: {
            toBasket() {
                this.$router.go(-1);
            },
            choiceFarmacy(pharmacy) {
                this.pharmacyForOrder = pharmacy;
                this.stateChoice = true;
            },
            choiceFarmacyBack(el) {
                this.stateChoice = el;
            },
            visibleAfterOrder(visibleState) {
                this.visibleButton = visibleState;
            },
            showMap() {
                this.showMapVisible = !this.showMapVisible;
            },
            choiceFarmacyFromMap(pharmacyFromMap) {
                this.pharmacyForOrder = pharmacyFromMap;
                this.stateChoice = true;

            }
        }
    }
</script>

<style scoped>
    .header {
        padding: 10px;
        margin-bottom: 10px;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
    }

    .header .title {
        align-self: center;
    }

    .checkout {
        font-size: calc(0.65em + 0.3vw);
    }

    .totalPrice {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: calc(0.65em + 0.3vw);
    }

    .price {
        font-size: calc(0.99em + 0.3vw);
        font-weight: 600;
        font-style: italic;
    }

    .custom-icon {
        width: 24px;
    }

    .table {
        font-size: calc(0.49em + 0.3vw);
    }


</style>