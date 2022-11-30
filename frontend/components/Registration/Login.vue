<template>
    <div class="holder">
        <h4>Log in</h4>
        <span class="welcome">Welcome to PhlowAi, please put your login credentials below to start using your chat bot</span>
        <div class="input-box">
            <div class="input-holder">
                <Label for="email">E-mail</Label>
                <input type="email" name="email" placeholder="JohnDoe@gmail.com" />
            </div>
            <div class="input-holder">
                <Label for="password">Password</Label>
                <input type="password" name="password" placeholder="********" />
            </div>
        </div>
        <div class="forgot-password">
            <a href="/">Forgot password</a>
        </div>
        <div class="btn-list">
            <div class="radio-btn inline-block">
                <input type="checkbox" name="Remember-me">
                <label for="Remember-me">Remember-me</label>
            </div>
            <button>Login</button>
        </div>
    </div>
</template>