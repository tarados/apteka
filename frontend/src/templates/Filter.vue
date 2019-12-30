<template>
    <div class="filtered">
        {{productList[0]}}
        <b-form-group class="inline-group">
            <b-form-checkbox-group
                    v-model="selected"
                    :options="options"
                    name="flavour-1a"
            />
        </b-form-group>

        <b-form-group class="stacked">
            <b-form-checkbox-group
                    v-model="selected"
                    :options="options"
                    name="flavour-2a"
                    stacked
            />
        </b-form-group>
    </div>
</template>

<script>
    export default {
        name: "Filters",
        props: {
            productList: {
                type: Array
            }
        },
        data() {
            return {
                selected: [], // Must be an array reference!
                options: []
            }
        },
        methods: {
            createOptionsList() {
                this.options = this.options.concat(this.productList);
            }
        },
        mounted() {
            this.createOptionsList();
        }
    }
</script>

<style scoped>
    .filtered {
        margin: 5px;
    }

    .inline-group {
        display: none;
    }

    @media screen and (max-width: 992px) {
        .inline-group {
            display: inline;
        }

        .stacked {
            display: none;
        }
    }

</style>