<template>
    <li class="flex justify-between items-center py-2 px-4 m-4 rounded-md bg-slate-100 hover:cursor-pointer hover:text-green-600"
        @mouseover="isShowIcon = true" @mouseleave="isShowIcon = false">
        <span class="flex justify-center gap-3 items-center">
            <font-awesome-icon :icon="icon" class=" text-sm md:text-base lg:text-xl text-green-600" />
            <p class="text-xs md:text-sm lg:text-base">{{ title }}</p>
        </span>
        <font-awesome-icon icon="fa-solid fa-arrow-right" v-if="isShowIcon" />
    </li>
</template>

<script lang="ts">
export default {
    props: {
        title: {
            type: String,
            required: true,
        },
        icon: {
            type: String,
            required: true,
        },
    },
    data() {
        return {
            isShowIcon: false,
        }
    }
}
</script>