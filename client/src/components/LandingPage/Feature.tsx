import React from 'react';
import image1 from './assets/images/1.jpg';
import image7 from './assets/images/7.jpg';
import image3 from './assets/images/3_.jpg';
import image66 from './assets/images/66.jpg';
import image5 from './assets/images/2.jpg';
import image55 from './assets/images/5.jpg';
import styles from './LandingPage.module.css';
import { useNavigate } from "react-router-dom";
import { Row, Col, Card } from 'antd';
const { Meta } = Card;

export const Feature = () => {
  const navigate = useNavigate();
  const onAdClick = (key) => {
    //navigate(key);
  }

  return (
    <div id="main-feature" className={styles.featureBlock}>
      <div className="container-fluid">
        <div className="titleHolder">
          <h2>Key Features and Benefits</h2>
          <p>
            Apart from many others, key features and benefits of using 360° Fitness!!
          </p>
        </div>
        <Row gutter={[16, 16]}>
          <Col xs={{ span: 24 }} sm={{ span: 12 }} md={{ span: 8 }} onClick={() => onAdClick('/fitnessplan')}>
            <Card hoverable cover={<img alt="Modern Design" src={image1} />}>
              <Meta title="Fitness at fingertips" />
            </Card>
          </Col>
          <Col xs={{ span: 24 }} sm={{ span: 12 }} md={{ span: 8 }} onClick={() => onAdClick('/search')}>
            <Card hoverable cover={<img alt="Test" src={image66} />}>
              <Meta title="Foods and Nutrition" />
            </Card>
          </Col>
          <Col xs={{ span: 24 }} sm={{ span: 12 }} md={{ span: 8 }} onClick={() => onAdClick('/diary')}>
            <Card hoverable cover={<img alt="Test" src={image55} />}>
              <Meta title="Food Diary" />
            </Card>
          </Col>
          <Col xs={{ span: 24 }} sm={{ span: 12 }} md={{ span: 8 }}>
            <Card hoverable cover={<img alt="Test" src={image7} />}>
              <Meta title="Workout plan" />
            </Card>
          </Col>
          <Col xs={{ span: 24 }} sm={{ span: 12 }} md={{ span: 8 }}>
            <Card hoverable cover={<img alt="Test" src={image3} />}>
              <Meta title="Great Support" />
            </Card>
          </Col>
          <Col xs={{ span: 24 }} sm={{ span: 12 }} md={{ span: 8 }}>
            <Card hoverable cover={<img alt="Test" src={image5} />}>
              <Meta title="Unlimited Features" />
            </Card>
          </Col>
        </Row>
      </div>
    </div>
  );
};
