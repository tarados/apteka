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
            filterableList: {
                type: Array
            },
            filterableField: {
                type: String
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
                this.filterableList.forEach((item) => {
                    item.text = item[this.filterableField];
                });
                // eslint-disable-next-line no-unused-vars
                const groupFilterableList = groupArray(this.filterableList, 'text');
                const keys = [];
                for (const key in groupFilterableList) {
                    keys.push(key);
                }
                this.options = this.options.concat(keys);
            },
            selectedItem() {
                this.$emit("filteredItem", this.selected);
            }
        },
        mounted() {
            this.createOptionsList();
        },
        watch: {
            selected: function () {
                this.selectedItem();
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