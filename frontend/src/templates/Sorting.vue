<template>
    <div class="sort-list">
        <div class="counter">
            <span>Товаров: {{ count }}</span>
        </div>
        <div class="sorting">
            <b-dropdown
                    split
                    split-variant="outline-info"
                    variant="info"
                    :text="text"
                    class="m-2"
            >
                <b-dropdown-item @click="sortingFromMin">От дешевых</b-dropdown-item>
                <b-dropdown-item @click="sortingFromMax">От дорогих</b-dropdown-item>
            </b-dropdown>
            <button type="button" @click="filterProduct" class="btn btn-danger">
                <custom-icon name="filter" class="custom-icon"/>
                <span>Фильтр</span>
            </button>
        </div>
    </div>
</template>

<script>
    import customIcon from 'vue-icon/lib/vue-feather.esm'

    export default {
        name: "Sorting",
        components: {
            // eslint-disable-next-line vue/no-unused-components
            customIcon
        },
        props: {
            product: {
                type: Object
            },
            count: Number
        },
        data() {
            return {
                text: "По релевантности"
            }
        },
        methods: {
            sortingFromMin() {
                this.text = "От дешевых";
                this.$emit("sortingProductPrice", 'min');
            },
            sortingFromMax() {
                this.text = "От дорогих";
                this.$emit("sortingProductPrice", 'max');
            },
            filterProduct() {
                this.$emit("filterProduct", "filter");
            }
        }
    }
</script>

<style scoped>
    .sort-list {
        display: flex;
        flex-wrap: nowrap;
        justify-content: space-between;
        align-items: center;
        margin: 0 5px;
    }

    .custom-icon {
        width: 24px;
    }

    .counter span {
        margin-left: 5px;
        color: #4d4d4d;
        font-size: 16px;
    }

</style>