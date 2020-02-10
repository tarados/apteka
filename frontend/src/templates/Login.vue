<template>
    <div class="contentLogin">
        <div class="labelLogin">
            <span>
                {{visible ? 'Введите, пожалуйста, Ваши контактные данные:'
                : 'Ваша заявка принята!'
                }}

            </span>
        </div>
        <validation-observer ref="observer" v-slot="{ passes }">
            <b-form @submit.stop.prevent="passes(onSubmit)">
                <validation-provider
                        name="Name"
                        :rules="{ required: true, min: 3 }"
                        v-slot="validationContext"
                >
                    <b-form-group id="example-input-group-1" label="Имя" label-for="example-input-1">
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
                    <b-form-group id="example-input-group-2" label="Фамилия" label-for="example-input-2">
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
                        :rules="{ required: true, regex: /^[0-9]+$/, min: 10 }"
                        v-slot="validationContext"
                >
                    <b-form-group id="example-input-group-3" label="Номер телефона" label-for="example-input-2">
                        <b-form-input
                                id="example-input-3"
                                name="example-input-3"
                                v-model="form.phone"
                                :state="getValidationState(validationContext)"
                                aria-describedby="input-1-live-feedback"
                        ></b-form-input>

                        <b-form-invalid-feedback id="input-1-live-feedback">{{ validationContext.errors[0] }}
                        </b-form-invalid-feedback>
                    </b-form-group>
                </validation-provider>
                <div class="buttonLogin">
                    <b-button type="submit" variant="success">Заказать</b-button>
                </div>

            </b-form>
        </validation-observer>
    </div>
</template>

<script>
    // import axios from 'axios'
    import * as send from '../send'
    export default {
        name: "Login",
        data() {
            return {
                form: {
                    name: null,
                    surname: null,
                    phone: null
                },
                visible: true
            };
        },
        methods: {
            getValidationState({dirty, validated, valid = null}) {
                return dirty || validated ? valid : null;
            },
            resetForm() {
                this.form = {
                    name: null,
                    surname: null,
                    phone: null
                };

                this.$nextTick(() => {
                    this.$refs.observer.reset();
                });
            },
            async onSubmit() {
                const response = await send.post("orders", this.form);
                // eslint-disable-next-line no-console
                console.log(response);
                if (response) {
                    this.visible = !this.visible;
                }
                this.form = {
                    name: null,
                    surname: null,
                    phone: null
                };

                this.$nextTick(() => {
                    this.$refs.observer.reset();
                });
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
</style>