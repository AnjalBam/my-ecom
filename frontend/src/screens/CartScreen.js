import React, { useEffect } from "react";
import { Link } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import {
    Row,
    Col,
    ListGroup,
    Image,
    Form,
    Button,
    Card,
} from "react-bootstrap";
import Message from "../components/Message";
import { addToCart, removeFromCart } from "../actions/cartActions";

const CartScreen = ({ match, location, history }) => {
    const productId = match.params.id;
    const qty = location.search ? Number(location.search.split("=")[1]) : 1;
    const dispatch = useDispatch();
    const cart = useSelector((state) => state.cart);
    const { cartItems } = cart;
    // console.log({  cartItems  });;
    useEffect(() => {
        if (productId) {
            dispatch(addToCart(productId, Number(qty)));
        }
    }, [dispatch, productId, qty]);

    const removeFromCartHandler = (id) => {
        dispatch(removeFromCart(id));
    };

    const checkoutHandler = () => {
        history.push("/login?redirect=shipping");
    };

    return (
        <Row>
            <Col md={8}>
                <h1>Shopping Cart</h1>
                {cartItems.length <= 0 ? (
                    <Message variant="info">
                        Your Cart is empty. <Link to="/">Go Back</Link>
                    </Message>
                ) : (
                    <ListGroup variant="flush">
                        {cartItems.map((cartItem) => (
                            <ListGroup.Item key={cartItem.product}>
                                <Row>
                                    <Col md={2}>
                                        <Image
                                            fluid
                                            rounded
                                            alt={cartItem.name}
                                            src={cartItem.image}
                                        />
                                    </Col>
                                    <Col md={3}>
                                        <Link
                                            to={`/product/${cartItem.product}`}
                                        >
                                            {cartItem.name}
                                        </Link>
                                    </Col>
                                    <Col md={2}>${cartItem.price}</Col>
                                    <Col md={3}>
                                        <Form.Control
                                            as="select"
                                            value={cartItem.qty}
                                            onChange={(e) =>
                                                dispatch(
                                                    addToCart(
                                                        cartItem.product,
                                                        e.target.value
                                                    )
                                                )
                                            }
                                        >
                                            {[
                                                ...Array(
                                                    cartItem.countInStock
                                                ).keys(),
                                            ].map((count) => (
                                                <option
                                                    key={count}
                                                    value={count + 1}
                                                >
                                                    {count + 1}
                                                </option>
                                            ))}
                                        </Form.Control>
                                    </Col>
                                    <Col md={1}>
                                        <Button
                                            type="button"
                                            variant="light"
                                            onClick={() =>
                                                removeFromCartHandler(
                                                    cartItem.product
                                                )
                                            }
                                        >
                                            <i className="fas fa-trash"></i>
                                        </Button>
                                    </Col>
                                </Row>
                            </ListGroup.Item>
                        ))}
                    </ListGroup>
                )}
            </Col>
            <Col md={4}>
                <Card>
                    <ListGroup variant="flush">
                        <ListGroup.Item>
                            <h2>
                                SubTotal (
                                {cartItems.reduce(
                                    (acc, item) =>
                                        (acc = Number(acc) + Number(item.qty)),
                                    0
                                )}
                                ) Items
                            </h2>
                            <h3>
                                {cartItems
                                    .reduce(
                                        (acc, item) =>
                                            (acc =
                                                Number(acc) +
                                                Number(item.qty * item.price)),
                                        0
                                    )
                                    .toFixed(2)}
                            </h3>
                        </ListGroup.Item>
                        <ListGroup.Item>
                            <Button
                                type="button"
                                className="btn btn-block"
                                disabled={cartItems.length === 0}
                                onClick={checkoutHandler}
                            >
                                Proceed To Checkout
                            </Button>
                        </ListGroup.Item>
                    </ListGroup>
                </Card>
            </Col>
        </Row>
    );
};

export default CartScreen;
