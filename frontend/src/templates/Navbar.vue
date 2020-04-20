<template>
    <div>
        <b-navbar toggleable="lg" type="light" variant="light">
            <b-navbar-brand href="#">
                <img src="../assets/logo.png" alt="brand">
            </b-navbar-brand>
            <b-navbar-toggle target="nav-collapse"/>
            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav class="mx-auto">
                    <b-nav-form>
                        <b-input-group size="sm" class="seachInput">
                            <b-form-input v-model="texts" placeholder="Search"/>
                        </b-input-group>
                    </b-nav-form>
                    <b-nav-item
                            :class="{ countVisible: !isCount }"
                            :to="{ path: '/basket'}" append
                    >
                        <custom-icon name="shopping-cart" class="custom-icon"/>
                        <b-nav-text>{{getCount}}</b-nav-text>
                    </b-nav-item>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    </div>
</template>

<script>
    import customIcon from 'vue-icon/lib/vue-feather.esm'
    import {mapGetters} from 'vuex'

    export default {
        name: "Navbar",
        components: {
            customIcon
        },
        data() {
            return {
                texts: '',
                isCount: false
            }
        },
        computed: {
            ...mapGetters(["allProducts"]),
            getCount() {
                const count = this.allProducts.length ? this.allProducts.length : 0;
                if (count > 0) {
                    this.isCount = true;
                }
                return count;
            },
        },
        methods: {
            getParam(texts) {
                this.$router.push({path: '/product/' + encodeURI(texts), params: encodeURI(texts)});
            }
            ,
            getParamOut() {
                this.$router.push({path: '/', params: 'empty'}).catch(err => {
                });
            },
            toBasket() {
                this.$router.push('/basket');
            }
        },
        mounted() {
            this.getParamOut();
        },
        watch: {
            texts: function (seach) {
                if (this.timerId) {
                    clearTimeout(this.timerId);
                }
                this.timerId = setTimeout(() => {
                    if (seach === '')
                        this.getParamOut();
                    else
                        this.getParam(seach);
                    this.timerId = 0;
                }, 1000);
            }
        }
    }
</script>

<style scoped>
    .seachInput {
        margin: 0 auto;
    }

    .custom-icon, .basket-icon{
        width: 30px;
        display: inline-block;
    }

    .countVisible {
        display: none;
    }
</style>