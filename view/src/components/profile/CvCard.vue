<template>
    <li class="flex justify-between">
        <div class="flex gap-4 items-center">
            <font-awesome-icon icon="fa-solid fa-file" class="bg-slate-200 text-xl text-green-600 p-4 rounded-lg" />
            <span class="flex flex-col">
                <h2 class=" text-sky-900 font-semibold text-xs md:text-sm lg:text-base hover:cursor-pointer" v-if="!isEditting">{{ fileName }}
                </h2>
                <input type="text" class="px-2 py-1 mb-1 border border-sky-950" v-else :value="fileName" @input="$emit('update:fileName', ($event.target as HTMLInputElement).value)" />

                <p class="text-gray-500 text-xs md:text-sm" v-if="!isEditting">{{ time }}</p>
                <input type="text" class="px-2 py-1 mb-1 border border-sky-950 text-black" v-else :value="time" @input="$emit('update:time', ($event.target as HTMLInputElement).value)" />
                
            </span>
        </div>
        <font-awesome-icon icon="fa-solid fa-xmark" class="text-green-700 hover:cursor-pointer" @click="deleteCV(id)" v-if="isEditting"/>
    </li>
</template>

<script lang="ts">
    export default {
        emits: [
            "delete-cv",
            "update:time",
            "update:fileName"
        ],
        props: {
            id: {
                type: Number,
                required: true,
            },
            fileName: {
                type: String,
                required: true,
            },
            time: {
                type: String,
                required: true,
            },
            isEditting: {
                type: Boolean,
                default: false,
            }
        },
        methods: {
            deleteCV(id: Number) {
                this.$emit("delete-cv", id);
            },
        }
    }
</script>