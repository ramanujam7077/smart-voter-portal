/**
 * Smart Voter Portal - Interactive JavaScript
 * Handles navigation, FAQ accordions, instant search, document checklist, and date picker safety.
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Mobile Menu Toggle
  const navToggle = document.getElementById('mobileNavToggle');
  const navLinks = document.getElementById('navLinks');

  if (navToggle && navLinks) {
    navToggle.addEventListener('click', () => {
      navLinks.classList.toggle('open');
      const isExpanded = navLinks.classList.contains('open');
      navToggle.setAttribute('aria-expanded', isExpanded);
    });
  }

  // 2. Date of Birth Picker Safety & Constraints
  const dobInput = document.getElementById('dob');
  if (dobInput) {
    const today = new Date();
    const yyyy = today.getFullYear();
    const mm = String(today.getMonth() + 1).padStart(2, '0');
    const dd = String(today.getDate()).padStart(2, '0');
    dobInput.max = `${yyyy}-${mm}-${dd}`;
    dobInput.min = `${yyyy - 110}-01-01`;
  }

  // 3. FAQ Accordion Logic
  const accordionButtons = document.querySelectorAll('.faq-question-btn');
  accordionButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const parentItem = btn.closest('.faq-accordion-item');
      if (parentItem) {
        const isOpen = parentItem.classList.contains('open');
        // Close others in group for cleaner view
        document.querySelectorAll('.faq-accordion-item').forEach(item => {
          if (item !== parentItem) item.classList.remove('open');
        });
        parentItem.classList.toggle('open', !isOpen);
      }
    });
  });

  // 4. FAQ Instant Search Filter
  const faqSearchInput = document.getElementById('faqSearchInput');
  if (faqSearchInput) {
    faqSearchInput.addEventListener('input', (e) => {
      const term = e.target.value.toLowerCase().trim();
      const faqItems = document.querySelectorAll('.faq-accordion-item');
      let visibleCount = 0;

      faqItems.forEach(item => {
        const question = item.querySelector('.faq-question-btn')?.textContent.toLowerCase() || '';
        const answer = item.querySelector('.faq-answer-panel')?.textContent.toLowerCase() || '';

        if (question.includes(term) || answer.includes(term)) {
          item.style.display = 'block';
          visibleCount++;
        } else {
          item.style.display = 'none';
        }
      });

      const noResultsBox = document.getElementById('faqNoResults');
      if (noResultsBox) {
        noResultsBox.style.display = visibleCount === 0 ? 'block' : 'none';
      }
    });
  }

  // 5. Interactive Document Checklist Progress
  const docCheckboxes = document.querySelectorAll('.doc-checklist-checkbox');
  const checklistCounter = document.getElementById('checklistCounter');
  
  function updateChecklistProgress() {
    if (!checklistCounter || docCheckboxes.length === 0) return;
    const checked = Array.from(docCheckboxes).filter(cb => cb.checked).length;
    checklistCounter.textContent = `${checked} of ${docCheckboxes.length} items checked`;
    if (checked >= 2) {
      checklistCounter.className = 'badge badge-success';
    } else {
      checklistCounter.className = 'badge badge-neutral';
    }
  }

  if (docCheckboxes.length > 0) {
    docCheckboxes.forEach(cb => {
      cb.addEventListener('change', updateChecklistProgress);
    });
    updateChecklistProgress();
  }
});
