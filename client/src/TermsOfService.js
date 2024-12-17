import React from "react";
import { Link } from "react-router-dom"; // Import Link for navigation
import './App.css';

const TermsOfService = () => {
  return (
    <div className="container">
      {/* Home Button */}
      <div className="home-button">
        <Link to="/">Home</Link>
      </div>

      <h1>Terms of Service</h1>
      <p>Last Updated: December 16, 2024</p>
      
      <section>
        <h2>1. Acceptance of Terms</h2>
        <p>
          By accessing and using Financial Fast Feed ("the Service"), you agree 
          to comply with and be bound by these Terms of Service. If you do not 
          agree, you may not use the Service.
        </p>
      </section>

      <section>
        <h2>2. Use of the Service</h2>
        <p>
          You agree to use the Service for lawful purposes only and refrain from:
        </p>
        <ul>
          <li>Violating any applicable local, state, or federal laws.</li>
          <li>Disrupting the Service or its associated servers/networks.</li>
          <li>Attempting to reverse-engineer or exploit any part of the Service.</li>
        </ul>
      </section>

      <section>
        <h2>3. Use of AI and Financial Information</h2>
        <p>
          Financial Fast Feed utilizes artificial intelligence to aggregate and summarize 
          financial news and content. This is provided strictly for informational purposes 
          and does not constitute financial advice, endorsements, or recommendations. 
        </p>
        <p>
          Users are advised to consult professional financial advisors before making 
          any investment decisions. The AI-generated summaries are based on publicly 
          available sources, and we do not guarantee their accuracy, completeness, 
          or reliability.
        </p>
        <p>
          Additionally, Financial Fast Feed does not own or claim to represent any third-party 
          sources from which content is aggregated. All source ownership remains 
          with the respective publishers.
        </p>
      </section>

      <section>
        <h2>4. Content and Copyright</h2>
        <p>
          All content provided through Financial Fast Feed is for informational 
          purposes only. The sources and articles are property of their respective 
          owners. We do not claim ownership or responsibility for any third-party content.
        </p>
      </section>

      <section>
        <h2>5. User Conduct</h2>
        <p>
          Users agree to interact with the Service responsibly and respectfully. Prohibited activities include, but are not limited to:
        </p>
        <ul>
          <li>Using bots, scripts, or automated methods to access the Service without authorization.</li>
          <li>Uploading malicious software, viruses, or harmful code.</li>
          <li>Engaging in scraping, data mining, or similar unauthorized data collection.</li>
          <li>Attempting to disrupt, overload, or interfere with the Service's functionality.</li>
        </ul>
        <p>
          Violating these terms may result in account termination or restricted access at the discretion of Financial Fast Feed.
        </p>
      </section>

      <section>
        <h2>6. Third-Party Links and Services</h2>
        <p>
          Financial Fast Feed may contain links to third-party websites, services, or content. These links are provided for 
          convenience and informational purposes only. We do not endorse, control, or take responsibility for the content 
          or policies of third-party sites. Accessing such links is at your own risk.
        </p>
      </section>

      <section>
        <h2>7. Disclaimer of Warranties</h2>
        <p>
          The Service is provided "as is" without warranties of any kind, 
          whether express or implied. We do not guarantee the accuracy, 
          completeness, or timeliness of the information provided.
        </p>
      </section>

      <section>
        <h2>8. Limitation of Liability</h2>
        <p>
          To the maximum extent permitted by law, Financial Fast Feed and its 
          creators shall not be held liable for any direct, indirect, or incidental 
          damages arising out of your use or inability to use the Service.
        </p>
      </section>

      <section>
        <h2>9. Indemnification</h2>
        <p>
          You agree to indemnify, defend, and hold harmless Financial Fast Feed, its creators, affiliates, and partners 
          from any claims, losses, damages, liabilities, or expenses (including legal fees) arising from your use of the Service, 
          your violation of these Terms, or any misuse of third-party content.
        </p>
      </section>

      <section>
        <h2>10. Termination</h2>
        <p>
          Financial Fast Feed reserves the right to suspend or terminate your access to the Service at any time, without notice, 
          for any reason, including but not limited to violations of these Terms of Service. Upon termination, you must cease 
          all use of the Service and delete any downloaded or printed materials obtained from it.
        </p>
      </section>

      <section>
        <h2>11. Governing Law</h2>
        <p>
          These Terms of Service shall be governed by and interpreted under the laws of British Columbia, Canada, 
          without regard to its conflict of law principles. You agree to submit to the exclusive jurisdiction of 
          the courts located in Vancouver, British Columbia for any disputes arising under or related to these Terms.
        </p>
      </section>

      <section>
        <h2>12. Changes to Terms</h2>
        <p>
          We reserve the right to update or modify these Terms at any time. 
          You are encouraged to review this page periodically for changes. 
          Continued use of the Service after updates constitutes acceptance 
          of the revised terms.
        </p>
      </section>

      <section>
        <h2>13. Contact Us</h2>
        <p>
          If you have any questions or concerns about these Terms of Service, 
          please contact us at: ethankcratchley@gmail.com
        </p>
      </section>
    </div>
  );
};

export default TermsOfService;
