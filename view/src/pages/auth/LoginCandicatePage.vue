<template>
    <section class="pt-20 bg-lime-50">
        <div
            class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0"
        >
            <a
                href="#"
                class="flex items-center mb-6 text-2xl font-semibold text-cyan-900"
            >
                Trang đăng nhập này dành riêng cho ứng viên
            </a>
            <div
                @submit.prevent="submitForm"
                class="w-full bg-gray- rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 bg-sky-200 dark:border-gray-700"
            >
                <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
                    <h1
                        class="text-xl font-bold leading-tight tracking-tight md:text-2xl text-cyan-900"
                    >
                        Đăng nhập vào tài khoản của bạn
                    </h1>
                    <form class="space-y-4 md:space-y-6" action="#">
                        <!-- email -->
                        <div class="form-control">
                            <label
                                for="email"
                                class="block mb-2 text-sm font-medium text-cyan-900"
                                >Email của bạn</label
                            >
                            <input
                                type="email"
                                name="email"
                                id="email"
                                class="bg-cyan-600 border border-gray-300 text-gray-300 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                placeholder="email@company.com"
                                v-model="emailCandicate.value"
                            />
                        </div>
                        <!-- password  -->
                        <div>
                            <label
                                for="password"
                                class="block mb-2 text-sm font-medium text-cyan-900"
                                
                                >Mật khẩu</label
                            >
                            <input
                                type="password"
                                name="password"
                                id="password"
                                placeholder="••••••••"
                                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                v-model="passwordCandicate.value"
                                @input="checkKeyDown"
                            />
                        </div>
                        <div>
                            <!-- <label v-if="checkKeyDown()"></label> -->
                            <label
                                class="block mb-2 text-sm font-medium text-red-500"
                                v-if="!passwordCandicate.isValid"
                                >Mật khẩu của bạn quá ngắn, hãy nhập lại mật
                                khẩu !</label
                            >
                        </div>
                        <!-- <div>
                        <label v-if="!formIsValid" class="block mb-2 text-sm font-medium text-red-500">Sai tài khoản đăng nhập hoặc mật khẩu, hãy điền lại !</label>
                    </div> -->
                        <!-- remember password  -->
                        <div class="flex items-center justify-between">
                            <div class="flex items-start">
                                <div class="flex items-center h-5">
                                    <input
                                        id="remember"
                                        aria-describedby="remember"
                                        v-model="
                                            rememberPasswordCandicate.value
                                        "
                                        type="checkbox"
                                        class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800"
                                    />
                                </div>
                                <div class="ml-3 text-sm">
                                    <label for="remember" class="text-cyan-900"
                                        >Nhớ mật khẩu</label
                                    >
                                </div>
                            </div>

                            <a
                                href="#"
                                class="text-sm font-medium text-primary-600 hover:underline dark:text-primary-500"
                                >Quên mật khẩu?</a
                            >
                        </div>

                        <button
                            type="submit"
                            class="w-full text-white bg-cyan-800 hover:bg-cyan-900 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2"
                        >
                            Đăng nhập
                        </button>

                        <p class="text-sm font-light text-cyan-800">
                            Bạn chưa có tài khoản ?
                            <a
                                href="#"
                                class="font-bold text-primary-600 hover:underline dark:text-primary-500"
                            >
                                <router-link to="./registerCandicatePage"
                                    >Đăng ký ngay !</router-link
                                >
                            </a>
                        </p>
                    </form>
                </div>
            </div>
        </div>
    </section>
</template>

<script lang="ts">
export default {
    data() {
        return {
            emailCandicate: {
                value: "",
                isValid: true,
            },
            passwordCandicate: {
                value: "",
                isValid: true,
                error: null,
            },
            rememberPasswordCandicate: {
                value: [],
                isValid: false,
            },
            formIsValid: true,
        };
    },
    methods: {
        validateForm() {
            this.formIsValid = true;
            if (this.emailCandicate.value === "") {
                this.emailCandicate.isValid = false;
                this.formIsValid = false;
            }
            if (
                this.passwordCandicate.value === "" ||
                this.passwordCandicate.value.length < 8
            ) {
                this.passwordCandicate.isValid = false;
                this.formIsValid = false;
            }
        },
        submitForm() {
            this.validateForm();
            if (!this.formIsValid) {
                return;
            }

            const formLoginCandicate = {
                first: this.emailCandicate,
                second: this.passwordCandicate,
                third: this.rememberPasswordCandicate,
            };
            console.log(formLoginCandicate);
        },
        checkKeyDown() {
            this.passwordCandicate.isValid = true;
        },
    },
    watch: {},
};
</script>