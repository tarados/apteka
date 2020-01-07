<template>
    <div class="filtered">
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
    import groupArray from 'group-array'

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
                this.productList.forEach(function (item) {
                   item.text = item.manufacturer;
                });
                // eslint-disable-next-line no-unused-vars
                const groupProductList = groupArray(this.productList, 'text');
                const keys = [];
                for (const key in groupProductList) {
                    keys.push(key);
                }
                this.options = this.options.concat(keys);
            },
            selectedManufacturer() {
                this.$emit("filteredManufacturer", this.selected);
            }
        },
        mounted() {
            this.createOptionsList();
        },
        watch: {
            selected: function () {
                this.selectedManufacturer();
            }
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