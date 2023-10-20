
<template>
    <section class="pt-20 bg-slate-50" v-for="company in companys">
        <card-company :company="company"></card-company>
    </section>
</template>

<script lang="ts">
    import companys from './data/company.ts'

    export default {
        component:{
            name:"card-company",
        },
        data() {
            return {
                companys: companys,
            }
        }
    }
</script>