<template>
    <section class="fixed top-0 left-0 right-0 h-full z-50 bg-white flex items-center justify-center">
    <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
        <a href="#" class="flex items-center mb-6 text-2xl font-semibold text-cyan-900">
            Trang đăng nhập này dành riêng cho nhân viên của các công ty tuyển dụng  
        </a>
        <div class="w-full bg-gray- rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 bg-sky-200 dark:border-gray-700">
            <div @submit.prevent="submitForm" class="p-6 space-y-4 md:space-y-6 sm:p-8 ">
                <h1 class="text-xl font-bold leading-tight tracking-tight  md:text-2xl text-cyan-900">
                    Đăng nhập vào tài khoản của bạn
                </h1>
                <form class="space-y-4 md:space-y-6" action="#">
                    <div>
                        <label for="email" class="block mb-2 text-sm font-medium text-cyan-900">Email của công ty</label>
                        <input type="email" name="email" id="email" class="bg-cyan-600 border border-gray-300 text-gray-300 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="company-name@email.com" required="true" v-model='emailCompanyName.value'>
                    </div>
                    <div>
                        <label for="email" class="block mb-2 text-sm font-medium text-cyan-900">Email của bạn</label>
                        <input type="email" name="email" id="email" class="bg-cyan-600 border border-gray-300 text-gray-300 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="email@company.com" required="true" v-model="emailEmployee.value">
                    </div>
                    <div>
                        <label for="password" class="block mb-2 text-sm font-medium text-cyan-900">Mật khẩu</label>
                        <input
                                type="password"
                                name="password"
                                id="password"
                                placeholder="••••••••"
                                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                v-model="passwordEmployee.value"
                                @input="checkKeyDown"
                            />
                    </div>
                    <div>
                            <label
                                class="block mb-2 text-sm font-medium text-red-500"
                                v-if="!passwordEmployee.isValid"
                                >Mật khẩu của bạn quá ngắn, hãy nhập lại mật
                                khẩu !</label
                            >
                        </div>
                    <div class="flex items-center justify-between">
                        <div class="flex items-start">
                            <div class="flex items-center h-5">
                              <input id="remember" aria-describedby="remember" type="checkbox" class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800"
                              v-model="rememberPasswordEmployee.value" >
                            </div>
                            <div class="ml-3 text-sm">
                              <label for="remember" class="text-cyan-900">Nhớ mật khẩu</label>
                            </div>
                        </div>
                        <a href="#" class="text-sm font-medium text-primary-600 hover:underline dark:text-primary-500">Quên mật khẩu?</a>
                    </div>

                    <button type="submit" class="w-full text-white bg-cyan-800 hover:bg-cyan-900 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 ">Đăng nhập</button>


                    <p class="text-sm font-light text-cyan-800">
                        Bạn chưa có tài khoản ? Hãy <a href="#" class="font-bold text-primary-600 hover:underline dark:text-primary-500">
                            <router-link to="./registerEmployeePage">đăng ký ngay !</router-link>
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
            emailCompanyName:{
                value: "",
                isValid: true,
            },
            emailEmployee: {
                value: "",
                isValid: true,
            },
            passwordEmployee: {
                value: "",
                isValid: true,
                error: null,
            },
            rememberPasswordEmployee: {
                value: [],
                isValid: false,
            },
            formIsValid: true,
        };
    },
    methods: {
        validateForm() {
            this.formIsValid = true;
            if(this.emailCompanyName.value === ""){
                this.emailCompanyName.isValid = false; 
                this.formIsValid = false; 
            }
            if (this.emailEmployee.value === "") {
                this.emailEmployee.isValid = false;
                this.formIsValid = false;
            }
            if (
                this.passwordEmployee.value === "" ||
                this.passwordEmployee.value.length < 8
            ) {
                this.passwordEmployee.isValid = false;
                this.formIsValid = false;
            }
        },
        submitForm() {
            this.validateForm();
            if (!this.formIsValid) {
                return;
            }

            const formLoginEmployee = {
                first: this.emailCompanyName,
                second: this.emailEmployee,
                third: this.passwordEmployee,
                last: this.rememberPasswordEmployee,
            };
            console.log(formLoginEmployee);
        },
        checkKeyDown() {
            this.passwordEmployee.isValid = true;
        },
    },
    watch: {},
};
</script>