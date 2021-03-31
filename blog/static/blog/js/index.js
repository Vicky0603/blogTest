/* Display chosen by <input> file in <img> and clear all on <button> click
*/
class FeaturedImagePreview {
    constructor(inputElement, imgElement, buttonElement) {
        this.imgInput = inputElement;
        this.imgPreview = imgElement;
        this.clearBtn = buttonElement;
    }

    mount() {
        this.setPreviewVisibility(false);

        this.imgInput.addEventListener('change', () => {
            this.onFileChange();
        });
        this.clearBtn.addEventListener('click', () => {
            this.clearAll();
        });
    }

    onFileChange() {
        const file = this.imgInput.files && this.imgInput.files[0];
        if (!file) {
            return;
        }
        
        this.imgPreview.src = URL.createObjectURL(file);
        this.setPreviewVisibility(true);
    }

    clearAll() {
        this.setPreviewVisibility(false);

        URL.revokeObjectURL(this.imgPreview.src);
        this.imgPreview.src = '';
        this.imgInput.value = null;
    }

    setPreviewVisibility(visible) {
        this.imgPreview.hidden = !visible;
        this.clearBtn.hidden = !visible;

        // FIXME: this is not obvious to user
        this.imgInput.parentElement.hidden = visible;
    }
}

document.addEventListener('readystatechange', (event) => {
    if (event.target.readyState === 'complete') {
        // initialize featured image preview
        document.querySelectorAll('[data-image-preview]').forEach((container) => {
            const imgInput = container.querySelector(container.dataset.selFileInput);
            const imgPreview = container.querySelector(container.dataset.selImg);
            const clearBtn = container.querySelector(container.dataset.selClearBtn);
            
            new FeaturedImagePreview(imgInput, imgPreview, clearBtn).mount();
        });
    }
});
