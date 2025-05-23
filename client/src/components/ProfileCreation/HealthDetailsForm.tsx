import styles from './ProfileCreation.module.css';
import React from "react";
import { Form, Row, Select } from "antd";

const { Option } = Select;

class HealthDetailsFormEl extends React.Component<any, any> {
    componentDidMount() {
        const { form, initialValues } = this.props;
        if (initialValues && initialValues.user_health_details) {
            form.setFieldsValue(initialValues.user_health_details);
        }
    }

    /** Method to validate and return transformed values */
    getFormattedValues = (callback) => {
        this.props.form.validateFields((err, values) => {
            if (!err) {
                const formattedValues = {
                    user_health_details: {
                        family_history: values.family_history || [],
                        existing_conditions: values.existing_conditions || [],
                        habitual_consumption: values.habitual_consumption || [],
                        current_medications: values.current_medications || [],
                        current_supplements: values.current_supplements || []
                    }
                };
                callback(null, formattedValues);
            } else {
                callback(err, null);
            }
        });
    };

    render() {
        const { getFieldDecorator } = this.props.form;
        const formItemLayout = {
            labelCol: { xs: { span: 6 }, sm: { span: 6 } },
            wrapperCol: { xs: { span: 12 }, sm: { span: 12 } },
        };

        const healthOptions = ["Diabetes", "Hypertension", "Heart Disease", "Asthma", "Stroke", "Cancer", "Kidney Disease", "Liver Disease", "Thyroid Disorder", "Arthritis", "Obesity", "COPD", "Alzheimer's", "Depression"];
        const consumptionOptions = ["Alcohol", "Cigarettes", "Caffeine", "Sugary Drinks", "Fast Food", "Processed Meat", "High Salt Intake", "High Sugar Intake", "Energy Drinks", "Recreational Drugs", "Red Meat", "Late Night Snacking", "Soft Drinks", "Excessive Dairy"];
        const medicationOptions = ["Amlodipine", "Metformin", "Lisinopril", "Atorvastatin", "Losartan", "Simvastatin", "Hydrochlorothiazide", "Levothyroxine", "Omeprazole", "Aspirin", "Warfarin", "Metoprolol", "Albuterol", "Gabapentin"];
        const supplementOptions = ["Multivitamins", "Protein Powder", "Omega-3", "Vitamin D", "Vitamin C", "Probiotics", "Collagen", "Magnesium", "Zinc", "Iron", "B-Complex", "Calcium", "Turmeric", "Ashwagandha"];

        return (
            <Form {...formItemLayout} className={styles.basicForm}>
                <Row gutter={24}>
                    <Form.Item label="Family History">
                        {getFieldDecorator("family_history")(
                            <Select placeholder="Select" mode="multiple" >
                                {healthOptions.map(option => (
                                    <Option key={option} value={option}>{option}</Option>
                                ))}
                            </Select>
                        )}
                    </Form.Item>
                    <Form.Item label="Existing Conditions">
                        {getFieldDecorator("existing_conditions")(
                            <Select mode="multiple" placeholder="Select conditions">
                                {healthOptions.map(option => (
                                    <Option key={option} value={option}>{option}</Option>
                                ))}
                            </Select>
                        )}
                    </Form.Item>
                    <Form.Item label="Habitual Consumption">
                        {getFieldDecorator("habitual_consumption")(
                            <Select mode="multiple" placeholder="Select habits">
                                {consumptionOptions.map(option => (
                                    <Option key={option} value={option}>{option}</Option>
                                ))}
                            </Select>
                        )}
                    </Form.Item>
                    <Form.Item label="Current Medications">
                        {getFieldDecorator("current_medications")(
                            <Select mode="multiple" placeholder="Select medications">
                                {medicationOptions.map(option => (
                                    <Option key={option} value={option}>{option}</Option>
                                ))}
                            </Select>
                        )}
                    </Form.Item>
                    <Form.Item label="Current Supplements">
                        {getFieldDecorator("current_supplements")(
                            <Select mode="multiple" placeholder="Select supplements">
                                {supplementOptions.map(option => (
                                    <Option key={option} value={option}>{option}</Option>
                                ))}
                            </Select>
                        )}
                    </Form.Item>
                </Row>
            </Form>
        );
    }
}

const HealthDetailsForm = Form.create()(HealthDetailsFormEl);
export default HealthDetailsForm;
