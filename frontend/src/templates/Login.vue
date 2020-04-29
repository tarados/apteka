<template>
    <div class="contentLogin">
        <validation-observer ref="observer" v-slot="{ passes }">
            <b-form @submit.stop.prevent="passes(onSubmit)">
                <b-form-group
                        v-if="visible"
                        label-cols-lg="3"
                        label="Контактные данные"
                        label-size="lg"
                        label-class="font-weight-bold pt-0"
                        class="mb-0"
                >
                    <validation-provider
                            name="Name"
                            :rules="{ required: true, min: 3 }"
                            v-slot="validationContext"
                    >
                        <b-form-group
                                id="example-input-group-1"
                                label="Имя:"
                                label-cols-sm="3"
                                label-align-sm="right"
                                label-for="example-input-1"
                        >
                            <b-form-input
                                    id="example-input-1"
                                    name="example-input-1"
                                    v-model="form.name"
                                    :state="getValidationState(validationContext)"
                                    aria-describedby="input-1-live-feedback"
                            ></b-form-input>

                            <b-form-invalid-feedback id="input-1-live-feedback">{{ validationContext.errors[0] }}
                            </b-form-invalid-feedback>
                        </b-form-group>
                    </validation-provider>
                    <validation-provider
                            name="SurName"
                            :rules="{ required: true, min: 3 }"
                            v-slot="validationContext"
                    >
                        <b-form-group
                                id="example-input-group-2"
                                label-cols-sm="3"
                                label="Фамилия:"
                                label-align-sm="right"
                                label-for="example-input-2"
                        >
                            <b-form-input
                                    id="example-input-2"
                                    name="example-input-2"
                                    v-model="form.surname"
                                    :state="getValidationState(validationContext)"
                                    aria-describedby="input-1-live-feedback"
                            ></b-form-input>

                            <b-form-invalid-feedback id="input-1-live-feedback">{{ validationContext.errors[0] }}
                            </b-form-invalid-feedback>
                        </b-form-group>
                    </validation-provider>
                    <validation-provider
                            name="Phone"
                            :rules="{ required: true, min: 15 }"
                            v-slot="validationContext"
                    >
                        <b-form-group
                                id="example-input-group-3"
                                label-cols-sm="3"
                                label="Номер телефона:"
                                label-align-sm="right"
                                label-for="example-input-2"
                        >
                            <b-form-input
                                    id="example-input-3"
                                    name="example-input-3"
                                    v-model="form.phone"
                                    @input="acceptNumber"
                                    :state="getValidationState(validationContext)"
                                    aria-describedby="input-1-live-feedback"
                            ></b-form-input>

                            <b-form-invalid-feedback id="input-1-live-feedback">{{ validationContext.errors[0] }}
                            </b-form-invalid-feedback>
                        </b-form-group>
                    </validation-provider>
                </b-form-group>
                <div class="buttonLogin" v-if="visible">
                    <b-button type="submit" variant="success">Заказать</b-button>
                </div>
            </b-form>
        </validation-observer>

    </div>
</template>

<script>
    import * as send from '../send'
    import * as basket from '../basket'
    import * as saveLogin from '../login'
    import {mapGetters} from 'vuex'

    export default {
        name: "Login",
        props: {
            pharmacyForOrder: {
                type: Object
            }
        },
        data() {
            return {
                form: saveLogin.getLogin(),
                visible: true
            };
        },
        computed: {
            ...mapGetters(["allProducts"]),
            ...mapGetters(["orderProductList"])
        },
        methods: {
            getValidationState({dirty, validated, valid = null}) {
                return dirty || validated ? valid : null;
            },
            async onSubmit() {
                this.form.order = this.orderProductList;
                this.form.pharmacyId = this.pharmacyForOrder.pharmacyId;
                const response = await send.post("order", this.form);
                if (response) {
                    this.visible = !this.visible;
                    basket.clearLocalStorage();
                    saveLogin.setLogin(this.form);

                }
                this.form = {
                    name: null,
                    surname: null,
                    phone: null
                };

                // this.$nextTick(() => {
                //     this.$refs.observer.reset();
                // });
                this.$emit('visibleAfterOrder', this.visible);
                this.$router.push('/successful');
            },
            acceptNumber() {
                let x = this.form.phone.replace(/\D/g, '').match(/(\d{0,3})(\d{0,3})(\d{0,2})(\d{0,2})/);
                this.form.phone = !x[2] ? x[1] : '(' + x[1] + ') ' + x[2] + (x[3] ? '-' + x[3] + '-' + x[4] : '');
            }
        }
    }
</script>

<style scoped>
    .contentLogin {
        margin: 20px 0;
        padding: 15px;
        border: 1px solid green;
        background-color: #f2f2f2;
        border-radius: 3px;
    }

    .labelLogin {
        margin: 20px 0;
        text-align: center;
    }

    .buttonLogin {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
    }

    .d-block {
        padding-left: 5px;
    }

    .orderSuccessful {
        text-align: center;
    }

    p {
        font-size: 25px;
        font-weight: 600;
        font-style: italic;
    }

    .form-row, .btn {
        font-size: calc(0.65em + 0.3vw);
    }
</style>