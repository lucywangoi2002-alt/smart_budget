// ===== DOCUMENT READY =====
document.addEventListener("DOMContentLoaded", function () {

    // =========================
    // 🔔 TOAST NOTIFICATIONS
    // =========================
    document.querySelectorAll('.toast').forEach(function (toastEl) {
        new bootstrap.Toast(toastEl, { delay: 3000 }).show();
    });

    // =========================
    // ✅ FORM VALIDATION
    // =========================
    document.querySelectorAll("form").forEach(form => {
        const submitBtn = form.querySelector("button[type='submit']");
        if (!submitBtn) return;

        function checkValidity() {
            submitBtn.disabled = !form.checkValidity();
        }

        form.addEventListener("input", checkValidity);
        checkValidity();
    });

    // =========================
    // 👁 PASSWORD TOGGLE
    // =========================
    document.querySelectorAll(".toggle-password").forEach(button => {
        button.addEventListener("click", function(e) {
            e.preventDefault();
            
            const input = this.closest(".input-group").querySelector("input");
            
            if (!input) {
                console.warn("No input found in this input-group");
                return;
            }
            
            if (input.type === "password") {
                input.type = "text";
                this.textContent = "🙈";
            } else {
                input.type = "password";
                this.textContent = "👁";
            }
        });
    });

    const passwordInput = document.querySelector('input[name="password1"]');
    const confirmPasswordInput = document.querySelector('input[name="password2"]');
    
    if (passwordInput) {
        // Add event listener for password input
        passwordInput.addEventListener('input', function() {
            const password = this.value;
            
            // Check each requirement
            const hasLength = password.length >= 8;
            const hasUpper = /[A-Z]/.test(password);
            const hasLower = /[a-z]/.test(password);
            const hasNumber = /[0-9]/.test(password);
            const hasSpecial = /[@$!%*?&]/.test(password);
            
            // Update requirement displays
            updateRequirement('req-length', hasLength);
            updateRequirement('req-upper', hasUpper);
            updateRequirement('req-lower', hasLower);
            updateRequirement('req-number', hasNumber);
            updateRequirement('req-special', hasSpecial);
            
            // Update password strength bar
            updateStrengthBar(password);
            
            // Also check password match if confirm password exists
            if (confirmPasswordInput && confirmPasswordInput.value) {
                checkPasswordMatch();
            }
        });
    }
    
    if (confirmPasswordInput) {
        confirmPasswordInput.addEventListener('input', function() {
            checkPasswordMatch();
        });
    }
    
    function updateRequirement(elementId, isValid) {
        const element = document.getElementById(elementId);
        if (element) {
            if (isValid) {
                element.classList.remove('invalid');
                element.classList.add('valid');
                element.querySelector('.requirement-icon').textContent = '✓';
            } else {
                element.classList.remove('valid');
                element.classList.add('invalid');
                element.querySelector('.requirement-icon').textContent = '◯';
            }
        }
    }
    
    function calculateStrength(password) {
        let strength = 0;
        if (password.length >= 8) strength++;
        if (/[A-Z]/.test(password)) strength++;
        if (/[a-z]/.test(password)) strength++;
        if (/[0-9]/.test(password)) strength++;
        if (/[@$!%*?&]/.test(password)) strength++;
        return strength;
    }
    
    function updateStrengthBar(password) {
        const strength = calculateStrength(password);
        const bar = document.getElementById('passwordStrengthBar');
        const text = document.getElementById('passwordStrengthText');
        
        if (bar && text) {
            const width = (strength / 5) * 100;
            bar.style.width = width + '%';
            
            if (password.length === 0) {
                bar.style.width = '0%';
                bar.className = 'progress-bar';
                text.textContent = 'Password strength: None';
                text.className = 'text-muted';
            } else if (strength <= 2) {
                bar.className = 'progress-bar bg-danger';
                text.textContent = 'Password strength: Weak';
                text.className = 'text-danger';
            } else if (strength <= 3) {
                bar.className = 'progress-bar bg-warning';
                text.textContent = 'Password strength: Fair';
                text.className = 'text-warning';
            } else if (strength <= 4) {
                bar.className = 'progress-bar bg-info';
                text.textContent = 'Password strength: Good';
                text.className = 'text-info';
            } else {
                bar.className = 'progress-bar bg-success';
                text.textContent = 'Password strength: Strong ✓';
                text.className = 'text-success';
            }
            
            // Add animation class for strength changes
            bar.style.transition = 'width 0.4s ease, background-color 0.3s ease';
        }
    }
    
    function checkPasswordMatch() {
        const password = passwordInput ? passwordInput.value : '';
        const confirmPassword = confirmPasswordInput ? confirmPasswordInput.value : '';
        
        // Remove existing match help text if any
        const existingHelp = document.querySelector('.password-match-help');
        if (existingHelp) {
            existingHelp.remove();
        }
        
        // Add match indicator if confirm password has value
        if (confirmPassword) {
            const helpDiv = document.createElement('div');
            helpDiv.className = 'password-match-help small mt-1';
            
            if (password !== confirmPassword) {
                helpDiv.className += ' text-danger';
                helpDiv.innerHTML = '✗ Passwords do not match';
                confirmPasswordInput.parentElement.parentElement.appendChild(helpDiv);
                
                // Add visual feedback to input fields
                confirmPasswordInput.style.borderColor = '#dc3545';
                if (passwordInput) passwordInput.style.borderColor = '#dc3545';
            } else {
                helpDiv.className += ' text-success';
                helpDiv.innerHTML = '✓ Passwords match';
                confirmPasswordInput.parentElement.parentElement.appendChild(helpDiv);
                
                // Add visual feedback to input fields
                confirmPasswordInput.style.borderColor = '#28a745';
                if (passwordInput) passwordInput.style.borderColor = '#28a745';
            }
        } else {
            // Reset border colors if no confirm password
            if (confirmPasswordInput) confirmPasswordInput.style.borderColor = '';
            if (passwordInput) passwordInput.style.borderColor = '';
        }
    }
    
    // Optional: Add tooltip for password strength
    const strengthBar = document.getElementById('passwordStrengthBar');
    if (strengthBar) {
        strengthBar.addEventListener('mouseenter', function() {
            const text = document.getElementById('passwordStrengthText');
            if (text && text.textContent.includes('Strong')) {
                this.title = 'Great! Your password is very secure.';
            } else if (text && text.textContent.includes('Good')) {
                this.title = 'Good password, but could be stronger.';
            } else if (text && text.textContent.includes('Weak')) {
                this.title = 'Add more variety to make your password stronger.';
            }
        });
    }
});