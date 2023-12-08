<template>
    <div class="py-8 px-16 bg-white rounded-lg flex justify-between items-center w-full">
        <font-awesome-icon :icon="icon"
            class="text-xl md:text-2xl lg:text-3xl xl:text-4xl p-4 rounded-full" :class="color"/>
        <span class="flex flex-col items-end gap-2">
            <h1 class="text-base md:text-lg lg:text-xl xl:text-2xl text-sky-900 font-semibold">{{ title }}</h1>
            <p class="text-xs md:text-sm lg:text-base text-slate-500">{{ subtitle }}</p>
        </span>
    </div>
</template>

<script lang="ts">
export default {
    props: {
        icon: {
            type: String,
            required: true
        },
        color: {
            type: String,
            required: true
        },
        title: {
            type: String,
            required: true
        },
        subtitle: {
            type: String,
            required: true
        }
    }
}
</script>