class OnionAgent:
    """
    Core OnionAgent for policy-driven, security-first child protection.
    Implements O.N.I.O.N: Observe, Notice, Infer, Operate, Narrate.
    """

    def __init__(self, config):
        # Initialize agent with configuration dict
        self.config = config
        self.guardian_notified = False
        self.audit_log = []

    def observe(self, input_data):
        # Observe and validate basic structure
        if not input_data or "user_id" not in input_data:
            self.narrate("Invalid input data: missing user_id.")
            return False
        self.narrate(f"Observed input from user {input_data['user_id']}")
        return True

    def notice(self, input_data):
        # Notice risks or policy violations
        if input_data.get("content", "").lower().strip() in ["badword", "harmful"]:
            self.narrate("Risk detected in user input.")
            return "risk"
        return "ok"

    def infer(self, risk_level):
        # Decide next steps based on risk
        if risk_level == "risk":
            self.operate("halt")
            return "Guardian alerted. Action halted."
        return "Proceed."

    def operate(self, operation):
        # Perform the operation
        if operation == "halt":
            self.guardian_notified = True
            self.narrate("Guardian has been notified due to risk.")
        else:
            self.narrate("Operation allowed.")

    def narrate(self, message):
        # Log and print events
        self.audit_log.append(message)
        print(f"[OnionAgent]: {message}")

    def process(self, input_data):
        # Main processing flow
        if not self.observe(input_data):
            return "Input rejected."
        risk = self.notice(input_data)
        decision = self.infer(risk)
        self.narrate(f"Decision outcome: {decision}")
        return decision
